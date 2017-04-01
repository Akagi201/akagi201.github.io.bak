+++
title = "在虚拟机上搭建OpenWrt平台"
date = "2014-03-25T03:18:08+08:00"
slug = "openwrt-on-virtual-machine"
githubIssuesID = 21

+++

## 1. OpenWrt平台搭建

### 1.1 环境准备

系统Debian7.4, 安装好官网buildroot说明的必备软件包 <http://wiki.openwrt.org/doc/howto/buildroot.exigence>

注意, 尽量使用较新的linux发行版, 因为openwrt比较新, 而且通常要在trunk分支下开发, 所以依赖的软件包都比较新, 避免繁琐的依赖关系问题.

### 1.2 编译固件

使用git或者svn下载源码
修改`feeds.conf.default`
然后更新软件索引

```
./scripts/feeds update –a
./scripts/feeds install –a
```

注意, 这里下载的知识编译固件用的控制文件(索引文件), 不包含源码.

然后运行make menuconfig(省去一些检查测试步骤, 具体可看官网说明), 这里注意3点:
1. Target system, 这个一定要选准.
2. Target Image, 选择固件image的格式, 这里我们准备在x86的VM上运行, 可以选择VMDK, 直接编译出硬盘文件, 并且包含grub.
3. 根据需要选择软件包, 要想通过web登录配置, 4个地方要选: Base system -> uci, Libraries -> libuci-lua, LuCI全选, Network -> uhttpd.

注意软件可以选择m或者y, 前者表示只编译出`xxx.ipk`安装包文件, 用户需要时将它上载到路由器中, `opkg install xxx.ipk` 安装, 后者表示直接编译在固件中.

最后运行make, 开始编译(可以使用make -j4 V=s加速编译和增加打印编译出错信息), 自动创建dl, build_dir两个目录, 依次调用tools, toolchain, package, target目录中的Makefile编译(前两者是工具, 然后用这个工具编译后两者). 自动根据指示下载所需的源码包, 放在dl目录下, 然后解压到build_dir目录中进行编译. build_dir中有3个子目录, host是于平台无关的一些工具, toolchain中式特定平台的工具, ulibc中式C库, 应用程序等.

### 1.3 VMware中运行OpenWrt

启动VMware, 新建虚拟机(custom), 以编译出的VMDK文件为硬盘, 直接power on就可以进入OpenWrt, 在目录/bin, /usr/bin等目录下, 有我们选择安装的应用程序的可执行文件, 运行他们实现各种功能.

## 2. 网络配置的简单示例

我们在虚拟机下运行, 虚拟机的网络模式有3种: nat, host-only, bridge. 我们安装完VMware后, 主机新增了2快虚拟网卡VMnet1, VMnet8, 前者相当于所有host-only模式的VM的交换机, 所有host-only模式的VM可通过它相互通信, 但不能与外界通信; 后者相当于素有nat模式的VM的交换机, 不同之处在于, 他可以NAT到主机的实际网口, 去访问外网(即相当于有个上行口(WAN口)), bridge模式指利用主机的实际网口与外界通信.

我们为OpenWrt的VM准备2块网卡, 一块是bridge模式, 另一块是host-only模式; 同时运行另一VM(red hat), 只有一块host-only模式的网卡, 如下图:

![openwrt-vmnet](http://akagi201.qiniudn.com/openwrt-vmnet.png)

OpenWrt的网络配置文件为`/etc/config/network`, 编辑写入:

```
configure interface lan
    option ifname eth0
    option proto dhcp
configure interface wan
    option igname eth1
    option proto dhcp
```

然后重启网络 `/etc/init.d/network restart`

再写入2条路由

```
Route add-net 10.10.10.0/24 dev eth0
Route add default dev eth1
```

再在VM-Redhat写入2条路由(注意: dev和gw的区别)

```
Route add-net 10.10.10.0/24 dev eth0
Route add default gw 10.10.10.130
```

这样, 实际局域网的主机就可通过OpenWrt这个路由器与host-only虚拟语句网的主机通信了, 当然前提是各主机应设一条网关路由到182.168.68.187

## 3. 应用程序开发

应用程序开发有2种方法.

### 3.1 方法一

利用menuconfig, 直接与固件一起编译, 即预先把相关文件放到 `trunk/package/myapp` 目录下, make menuconfig时就能找到该软件包, 选择(可以选y编译进固件中, 或m只编译成.ipk包)即可.

比如, 在package目录下mkdir hello world, 里面放些什么则至关重要, 可以参考其他包的内容, 其中的Makefile的最关键的, 其他都可选, 比如我们这里还放了一个src子目录, 里面放helloworld.c, Makefile(它是真正编译用的).

Makefile的内容可参考模板, 一般分为很多节, 第一节一般说明程序名称, 版本等; 第二节说明软件包的基本属性(他是一般包, 还是kernel包, SECTION, CATEGORY字段说明其在menuconfig中的位置, 一定要写准确, 该包的依赖关系等). 注意Makefile中Tab符不能乱用, 一般表示command, 这里的属性字段不用用Tab, 只能用空格.

后面几节描述了他的编译安装方法. 一般就是把src里的内容copy到build_dir/uClib下, 然后用toolchain来编译, 最后install一节可以指明该app在固件中被放在哪个目录下(/bin, 或 /usr/bin等).

### 3.2 方法二

利用SDK, 就像android开发一样, 利用sdk编译出软件安装包, 上传到设备, 安装即可使用. 首先在make menuconfig的时候, 把build SDK选项选上, 那么, 固件编译好后, 在trunk/bin/x86下就有一个SDK.tar文件, 解压, 进入里面.

可以发现里面的内容和trunk主目录下的非常相似, 也有package, buld_dir, dl等目录, 实际上它正是模拟了一个固件的编译环境, 这样就简单了, 如方法一所述, 在package目录下建立我们的app子目录, 放入必要的文件, 然后退回到SDK目录, 直接make即可, 编译好的.ipk包在SDK/bin/x86/package下.

至于上传.ipk包到路由器上, 对于实际设备, 可以scp工具, 在VMware下没找到更好的方法.

### 3.3 为什么要用ipk包

ilk包是openwrt特有的, 为什么用这个呢, 直接把可执行文件copy到设备中不就行了吗? 回头看看hello world中的Makefile的最后一节install就ming明白了, ilk包li里不仅有可执行文件, 还有安装该文件的具体指示, 甚至还有其他一些配置, 启动文件, 以及他们的安装方式.

联想network命令就是这样的, 进到package/conf下, 看他的Makefile最后, 其实就是拷贝文件.

## Refs
* <http://www.cnblogs.com/zmkeil/archive/2013/04/17/3027385.html>