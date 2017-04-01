+++
title = "Gdbserver On OpenWrt"
date = "2014-03-24T02:56:08+08:00"
slug = "gdbserver-on-openwrt"
githubIssuesID = 19

+++

编写的程序部署到OpenWrt上出错, 打日志是个好办法, 但是今天遇到的情况, 日志也不能显示出正确的程序流程, 实在诡异, 因此, 决定尝试调试器.

熟悉在普通的电脑上使用gdb调试的基本方法: <http://www.ibm.com/developerworks/linux/library/l-gdb/>

下载<gdb quick reference>2张纸, 打印出来放在手边备用.

路由器中的存储空间十分有限, OpenWRT的包管理器opkg提供的GDB占用大约1.5MB空间. 路由器本身有8M的存储空间, 目前只剩200KB了, GDB的大小不能接受. 相比之下, GDBServer的大小 不到100KB, 这是可以接受的.

## gdbserver远程调试方法

### 路由器端
1. 安装gdbserver

```
opkg install gdbserver
```

2. 进入目录, 运行gdbserver, 监听网络端口

```
gdbserver 192.168.8.1:4455 xxxx
```

### PC端
1. 根据OpenWrt SDK位置配置好PATH路径
2. 进入被调试的程序文件, 这是为了向gdb提供程序的调试信息.
3. 指定被调试的程序文件, 启动gdb.

```
mips-openwrt-linux-gdb xxxx
```

4. 在gdb中连接远程调试器

```
target remote 192.168.8.1:4455
```

5. 等待崩溃

```
bt
```

如果连接成功, 则此时就可以像平常一样使用gdb来调试程序了, 不过调试目标是位于路由器的程序. 使用这个方法可以很轻易的定位到程序错误的位置. 毕竟是动态调试.

## 编译gdb和gdbserver方法

```
# gdb的编译
cd ~/gdb/gdb-7.3.1
mkdir bin
cd bin
../configure --prefix=/opt/gdb-7.3.1 --host=i686-pc-linux-gnu --target=mips-linux
make
make install

# gdbserver的编译
cd ~/gdb/gdb-7.3.1/gdb/gdbserver
mkdir bin
cd bin
export CC=/opt/openwrt/kamikaze_7.09/staging_dir_mips/bin/mips-linux-gcc
../configure --target=mips-linux --host=mips-linux
make
```

## 补充

如果上面的方法不能工作, 有可能是openwrt设备上的库被stripped了, 可以在host主机上使用没有stripped的库来远程调试.

## openwrt源码上编译工具链
在menuconfig上enable gdb 和 gdbserver.

```
Advanced configuration options (for developers) → Toolchain Options → Build gdb
```

```
Utilities → gdbserver
```

## 给你想调试的包增加调试信息

1. 添加CFLAGS到你要调试的package的Makefile中.

```
TARGET_CFLAGS += -ggdb3
```

2. 重新编译package带有CONFIG_DEBUG.


```
make package/busybox/{clean,compile} V=99 CONFIG_DEBUG=y
```

3. 或者在menuconfig中使能debug info

```
Global build settings > Compile packages with debugging info
```

## Refs

* <https://sourceware.org/gdb/current/onlinedocs/gdb/>
* <http://h4x3rotab.github.io/blog/2014/02/27/openwrtxia-de-gdbyuan-cheng-diao-shi/>
* <http://blog.csdn.net/vastsmile/article/details/5614856>