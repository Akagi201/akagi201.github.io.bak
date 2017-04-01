+++
title = "在Mac OS X下配置OpenWrt Buildroot环境"
date = "2013-10-28T15:00:08+08:00"
slug = "openwrt-buildroot-on-macosx"
githubIssuesID = 6

+++

## 与linux相比会遇到的2个问题
1. OpenWrt需要一个case-sensitive filesystem, 而Mac OS X默认提供的文件系统是case-insensitive.
2. Mac OS X下缺少大量的开发工具包, 在普通linux下都有.
* 使用一个disk image(避免再次分区硬盘), 和Homebrew.

## steps
1. Disk Image Creation
hdiutil create -size 20g -fs "Case-sensitive HFS+" -volname OpenWrt OpenWrt.dmg
hdiutil attach OpenWrt.dmg
这个命令会在当前目录创建一个20GB image, 并且attach他名字为"OpenWrt", 执行后你会在Finder中看到OpenWrt volume, 是空的.
cd /Volumes/OpenWrt
2. Packages installation
有两种类型的packages:
* XCode framework: Apple development SDK
. 包含了core compilers和libraries.
* Homebrew framework: a package manager用来下载开源components到你的系统.
brew install coreutils e2fsprogs ossp-uuid asciidoc binutils bzip2 fastjar flex getopt gtk2 intltool jikes hs-zlib openssl p5-extutils-makemaker python26 subversion rsync ruby sdcc unzip gettext libxslt bison gawk autoconf wget gmake ncurses findutils
* missing: bzip2 getopt(gnu-getopt代替, 将mac os x自带的/usr/bin/getopt 重命名备份，把gnu-getopt链接到/usr/local/bin/getopt) gtk2 jikes zlib p5-extutils-makemaker tar(gnu-tar代替) python26(python代替) rsync unzip gmake ncurses

## Easy Build
不需要产生或下载不必要的packages.<http://wiki.openwrt.org/doc/howto/easy.build>

## Refs
* [Setup MacOSX as an OpenWrt build environment](http://wiki.openwrt.org/easy.build.macosx)
* [OpenWrt Buildroot – Installation on Mac OS X](http://wiki.openwrt.org/doc/howto/buildroot.exigence.macosx)
* <https://forum.openwrt.org/viewtopic.php?id=34676>
<http://digiland.tw/viewtopic.php?id=2105>
* <http://blog.csdn.net/mirkerson/article/details/7287931>
