#!/usr/bin/env python3

import json
import sys
import os

import requests

GITHUB_REPO = "akagi201.github.io"

s = requests.Session()

def github_list_issues():
  if 'GH_TOKEN' not in os.environ:
    print("Error: please set GH_TOKEN env var")
    sys.exit(1)
  token = os.environ['GH_TOKEN']
  headers = {'Authorization': "token " + token}
  url = 'https://api.github.com/repos/%s/issues' % GITHUB_REPO
  resp = s.get(url, headers=headers)
  content = json.loads(resp.content.decode('utf-8'))
  slug2ids = {}
  if content["message"] == "Not Found":
    return {}
  for issue in content:
    slug2ids[issue["title"]] = int(issue["number"])
  return slug2ids

def github_create_issue(subject, message):
  if 'GH_TOKEN' not in os.environ:
    return None
  token = os.environ['GH_TOKEN']
  data = {'title': subject, 'body': message}
  headers = {'Authorization': "token " + token}
  url = 'https://api.github.com/repos/%s/issues' % GITHUB_REPO
  resp = s.post(url, headers=headers, data=json.dumps(data))
  content = json.loads(resp.content.decode('utf-8'))
  return content["number"]

def extract_slug(path):
  slug, issueid = None, None
  with open(path) as fd:
    for line in fd:
      if line.startswith("slug"):
        slug = line[len("slug ="):-1].strip()
      if line.startswith("githubIssuesID"):
        issueid = int(line[len("githubIssuesID ="):-1].strip())
    return path, slug, issueid

def find_slugs():
  for root, _, files in os.walk("content/post"):
    for filename in files:
      if filename.endswith(".md"):
        filepath = os.path.join(root, filename)
        yield extract_slug(filepath)

def main():
  slug2ids = github_list_issues()
  for path, slug, issueid in find_slugs():
    if slug == None:
      print("ERROR: file %s don't have slug" % path)
      continue
    if slug in slug2ids:
      if issueid == None:
        print("WARN: file %s should have issueid %s" % (path, slug2ids[slug]))
        continue
      if issueid != slug2ids[slug]:
        print("ERROR: file %s with slug %s have id %s mismatch github id %s " %
         (path, slug, issueid, slug2ids[slug]))
        continue
    if issueid == None:
      message = "This issue is reserved for https://akagi201/post/%s" % slug
      newissueid = github_create_issue(slug, message)
      print("%s githubIssuesID %s" % (path, newissueid))
      slug2ids[slug] = newissueid
      continue

if __name__ == '__main__':
  main()