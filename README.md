
# akblog

## git subtree

1. 第一次添加子目录，建立与git项目的关联
`git subtree add --prefix=<子目录名> <子仓库名> <分支> --squash`
`git subtree add --prefix public git@github.com:Akagi201/akagi201.github.io.git master --squash`

2. 从远程仓库更新子目录
`git subtree pull --prefix=<子目录名> <远程分支> <分支> --squash`
`git subtree pull --prefix=public git@github.com:Akagi201/akagi201.github.io.git master --squash`

3. 从子目录push到远程仓库（确认你有写权限）
`git subtree push --prefix=<子目录名> <远程分支名> <分支>`
`git subtree push --prefix=public git@github.com:Akagi201/akagi201.github.io.git master`

## Build

```
git clone git@github.com:Akagi201/akblog.git
cd akblog
git clone --recursive https://github.com/spf13/hugoThemes.git themes
hugo server -t 'theme-name'
```

## Publish

1. manual method

```
// 在content添加md文件
$ hugo -t 'hyde' // 如果改动较大, 先rm -rf public/*
$ git add -A
$ git commit -m "update site" && git push origin master
$ git subtree push --prefix=public git@github.com:Akagi201/akagi201.github.io.git master
```

2. use deploy.sh

```
./deploy.sh "some update msg"
```
