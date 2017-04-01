+++
title = "git commit 规范"
date = "2014-03-24T01:32:08+08:00"
slug = "git-commit-convention"
githubIssuesID = 20

+++

最近发现自己的git log太乱了, 稍微整理一下规范.

## 基本原则
* 永远不在`git commit`后增加`-m <msg>`来添加日志. 直接git commit [-a]然后会出现一个编辑界面.
* 在.vimrc中添加一行, 来检查拼写和自动折行.

```
autocmd Filetype gitcommit setlocal spell textwidth=72
```

* 第一行应该少于50个字, **随后一个空行**, 然后写具体内容.

## 举例

* 总体格式

```
模块名: msg +补充信息关键字(time/issue/review) 补充信息(#issue号 可被github识别)
```

* 第一次提交用 `first blood`

* 记录花费时间2d 3h

```
othermsg +time 2d 3h
```

* 修issue: 1234

```
othermsg +issue #1234
```

* 提交的同时, 有代码审查, 审查人user1, user2

```
othermsg +review @user1 @user2
```

* 提交的同时, 和1112号代码审查相关联

```
othermsg +review 项目代码审查关键字-1112
```

任何项目管理工具(即使使用文本文件管理)都会很容易解析上述信息, 无论用的是git还是svn.

另外更详细的信息会在代码中或者项目管理工具中出现, 不需要提交太多"othermsg", 一两句概述的话或单词说清楚就行.

## Refs
* <http://segmentfault.com/q/1010000000395039>
* <http://ruby-china.org/topics/15737>