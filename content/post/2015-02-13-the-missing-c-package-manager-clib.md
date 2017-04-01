+++
title = "The Missing C Package Manager Clib"
date = "2015-02-12T07:44:08+08:00"
slug = "the-missing-c-package-manager-clib"
githubIssuesID = 46

+++

web与移动开发领域每种语言都有自己的包管理器. `nodejs`的`npm`, `golang`的`go get`, `lua`的`luarocks`, ios&macosx平台的`cocoapods`, `Python`的`Pip`&`Eggs`, `TeX`的`CTAN`, `Perl`的`CPAN`, `Java`的`Maven`, `Haskell`的`cabal`, `Ruby`的`Gems`, `.Net`的`NuGet`. 如果有兴趣, 可以看下这个播客<https://ipn.li/kernelpanic/7/>

不过C语言确一直没有一个这样的工具. 导致的问题就是, 当你需要用功C语言实现一个很通用的功能的时候, 你没有一个合适的地方去找, 只能google, stackoverflow, github去搜, 然后你有发现你要的这个功能在一个很大的项目里面的一个小模块, 然后很难独立提取出来, 然后只好重复造轮子.

还好, nodejs社区的几个人创造了Clib. C语言终于有自己的包管理器啦: Clib. TJ Holowaychuk先用node.js写了Clib, 然后Stephen Mathieson把他port成了C.

## Clib developer's blog
* [Introducing Clib](https://medium.com/code-adventures/introducing-clib-b32e6e769cb3)
* [The Advent of Clib: the C Package Manager](https://blog.ashworth.in/the-advent-of-clib-the-c-package-manager/)