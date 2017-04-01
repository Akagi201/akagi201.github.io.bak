+++
title = "学习State Threads"
date = "2015-03-10T12:35:08+08:00"
slug = "learning-state-threads"
githubIssuesID = 49

+++

<iframe src="https://atlas.mindmup.com/akagi201/learning_state_threads/index.html" width="600" height="300"></iframe>

State Threads(简称ST)是一个C语言轻量级用户层的线程库, 总共4631行C代码. 这个线程库有助于开发者实现一个具有高性能和可扩展性的网络应用程序. 是Apache项目里面的一个子项目.(?Apache以前听说是用的select啊, 可能apache最后没用st, 懒得去考证了)

```
akagi201@akrmbp ~/Documents/state-threads (master) $ cloc .
      41 text files.
      38 unique files.
      11 files ignored.

http://cloc.sourceforge.net v 1.62  T=0.22 s (139.8 files/s, 61376.1 lines/s)
---------------------------------------------------------------------------------------
Language                             files          blank        comment           code
---------------------------------------------------------------------------------------
C                                       16           1046           1174           4631
HTML                                     3            236              0           3822
C/C++ Header                             6            270            288            939
make                                     3            106            205            364
Assembly                                 1             31            161            239
Windows Module Definition                1              0              0             51
Bourne Shell                             1             10              9             26
---------------------------------------------------------------------------------------
SUM:                                    31           1699           1837          10072
---------------------------------------------------------------------------------------
```

## Docs
* 项目官方只有4页文档. <http://state-threads.sourceforge.net/docs/index.html>
* 其中introductory已经被好多国人翻译过了.(见下面Refs)

## Refs
* <http://coolshell.cn/articles/12012.html>
* <https://github.com/zfengzhen/Blog/blob/master/article/%E4%B8%BA%E4%BA%92%E8%81%94%E7%BD%91%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E8%80%8C%E7%94%9F%E7%9A%84State%20Threads%5B%E5%B8%B8%E8%A7%81%E5%90%8E%E5%8F%B0%E6%9E%B6%E6%9E%84%E6%B5%85%E6%9E%90%5D.md>
* <http://blog.csdn.net/win_lin/article/details/8242653>
* <https://github.com/wuyu201321060203/wuyu201321060203.github.io/blob/master/_posts/2014-10-15-ST.md>