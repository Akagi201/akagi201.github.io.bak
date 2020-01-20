+++
title = "A File-oriented C/C++ Dependency Manager Biicode"
date = "2015-03-16T04:45:08+08:00"
slug = "a-file-oriented-c-cpp-dependency-manager-biicode"

+++

Biicode is a file-oriented Dependencies Manager for C and C++ developers.

## Features
* 在C++中实现Go语言的modularity, 类似低是通过写合适的`#include`语句实现.
* 文件级别的依赖管理, 重用已有项目的任何独立文件.
* 使用一条命令分享和发布到biicode
* 不用打包, 直接使用源码进行模块管理.
* 基于CMake编译
* 支持依赖包的版本控制.
* biicode保存meta-data在文本文件中.

## docs
* <http://docs.biicode.com/c++.html>

## 基础命令
* 版本: `bii version`
* 检查并安装编译工具: `bii setup:cpp`
* 搜索依赖: `bii find`
* 编译: `bii cpp:build`
* 创建项目: `bii init myproject`, 生成`bii`目录
* 创建hello world项目: `bii new myuser/myblock --hello=cpp`, 生成`blocks`目录.
* 发布到biicode: `bii publish` 默认发布到`DEV`, 每次默认覆盖上次的`DEV`代码.
* Release life-cycle tags: DEV, ALPHA, BETA, STABLE. `bii publish --tag=STABLE`
* 清理编译生成的结果: `bii clean`
* 下载一个block到本地项目block中: `bii open owner/block_name`

## 吐槽
* 支持nodejs是什么鬼啊! 就算技术上能实现, 可不可以完善好C/C++再搞其他的.