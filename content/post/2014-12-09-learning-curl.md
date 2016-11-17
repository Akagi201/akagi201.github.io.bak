+++
title = "Learning cURL"
date = "2014-12-09T03:55:26+08:00"
slug = "learning-curl"

+++

<iframe src="https://atlas.mindmup.com/akagi201/learning_curl/index.html" height="100%" width = "100%"></iframe>

cURL全称是"Client for URLs", 即URL客户端.

是[Daniel Stenberg](https://github.com/bagder)的一个个人项目, 就放在个人的一个二级域名<http://curl.haxx.se/>下, 所以有的地方略显粗糙也可以理解了.

项目历史应该比较久远了, 文档全是用的`manpage`写的, 不用到处找了, 直接`man`就可以了.

`curl`的`repo`由两部分组成, `curl`命令行跟`libcurl`, 其中复杂的东西都在`libcurl`中了.

## 源码结构
* `curl`命令行的源码在`src/`, 入口在`tool_main.c`.
* `libcurl`的源码在`lib/`.
* `API example`的源码在`docs/examples`下.
