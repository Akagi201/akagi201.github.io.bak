+++
date = "2016-02-16T08:26:44+08:00"
title = "Reading Nginx tutorial"
slug = "reading-nginx-tutorial"

+++

这是一篇无聊的文章, 用于记录自己的阅读进度而已.

## 文档地址
* <https://openresty.org/download/agentzh-nginx-tutorials-zhcn.html>

## 进度

### 2016-02-16
* 指令 = 语句, 每行语句后有一个分号.
* 只有一种变量类型, 字符串.
* ngx_http_rewrite_module: <http://nginx.org/en/docs/http/ngx_http_rewrite_module.html>
* nginx第三方模块: <https://www.nginx.com/resources/wiki/modules/>
* HTTP Echo Module: <https://www.nginx.com/resources/wiki/modules/echo/> <https://github.com/openresty/echo-nginx-module>
* 疑问: 为什么叫第三方模块, 不过还是包含在nginx的官方发现版里了? 第三方模块融入nginx upstream的流程?
* 变量插值: variable interpolation (从Perl语法引入)
* 变量名前一律加$
* Nginx的语法是可扩展的? 通过添加一个第三方模块, 就可以增加指令, 增加语法?
* ngx_http_geo_module: <http://nginx.org/en/docs/http/ngx_http_geo_module.html>
* Nginx 变量的创建和赋值操作发生在全然不同的时间阶段。Nginx 变量的创建只能发生在 Nginx 配置加载的时候，或者说 Nginx 启动的时候；而赋值操作则只会发生在请求实际处理的时候。这意味着不创建而直接使用变量会导致启动失败，同时也意味着我们无法在请求处理时动态地创建新的 Nginx 变量。
* 读完 Nginx 变量漫谈（一）

### 2016-02-17
* echo_exec 内部跳转: <https://github.com/openresty/echo-nginx-module#echo_exec>
* Nginx 变量值容器的生命期是与当前正在处理的请求绑定的，而与 location 无关。
* ngx_http_rewrite_module: <http://nginx.org/en/docs/http/ngx_http_rewrite_module.html>
* ngx_http_core_module: <http://nginx.org/en/docs/http/ngx_http_core_module.html>
* Set Misc: <https://github.com/openresty/set-misc-nginx-module#set_unescape_uri>
* 读完 Nginx 变量漫谈（二）

### 2016-02-19
* ngx_http_proxy_module: <http://nginx.org/en/docs/http/ngx_http_proxy_module.html>
* 不是所有的 Nginx 变量都拥有存放值的容器。拥有值容器的变量在 Nginx 核心中被称为“被索引的”（indexed）；反之，则被称为“未索引的”（non-indexed）。
* 读完 Nginx 变量漫谈（三）
* 读完 Nginx 变量漫谈 (四)
* Nginx 变量值容器的生命期是与当前请求相关联的。每个请求都有所有变量值容器的独立副本，只不过当前请求既可以是“主请求”，也可以是“子请求”。即便是父子请求之间，同名变量一般也不会相互干扰。
* Module ngx_http_auth_request_module: <http://nginx.org/en/docs/http/ngx_http_auth_request_module.html>
* Nginx 变量漫谈（五）

### 2016-02-22
*
