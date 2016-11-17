#!/bin/bash

echo -e "\033[0;32mDeploying updates to Github...\033[0m"

GIT_DEPLOY_REPO="git@github.com:Akagi201/akagi201.github.io.git"

# Build the project.
hugo -t 'kami'

cd public

rm -rf .git

git init

git add .

# Commit changes.
msg="rebuilding site `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

git push --force "${GIT_DEPLOY_REPO}" master
