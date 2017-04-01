+++
title = "移植linux内核的list.h到用户态"
date = "2015-03-18T08:32:26+08:00"
slug = "port-list_h-in-kernel-to-userspace"
githubIssuesID = 53

+++

以前工作的时候在项目里使用过的, 随着离职, 代码已经无法找到了. :(

没关系这次放到github上面就不会丢失了.

## Features
* Type Oblivious
* Portable
* Easy to Use
* Readable
* Saves Time

## Usages
* List is inside the data item you want to link together.
* You can put `struct list_head` anywhere in your structure.
* You can name `struct list_head` variable anything you wish.
* You can have multiple lists!

## Repo
* <https://github.com/Akagi201/list>

## Refs
* <http://isis.poly.edu/kulesh/stuff/src/klist/>