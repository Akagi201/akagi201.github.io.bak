+++
title = "About"
date = "2014-03-08T02:37:08+08:00"
slug = "openwrt-10-years"
githubIssuesID = 12

+++

如果不是为了写这篇文章, 笔者还真没意识到OpenWrt这个项目已经10年了.

在这个重新强调人工智能, 机器学习, 重新重视物理机械交互的新兴智能机器人的时代, 我们有理由相信因为其纯正的Linux味道, 小型化, 亲近物理交互的特征, 身为Linux社区与物理交互的最佳桥梁, OpenWrt会迎来新一轮的发展.

一切都始于2002年12月, Linksys发布了定义家用无线路由器产品形态的WRT54G, 由于成本的原因, Linksys使用Linux作为固件而不是授权费用很高的VxWorks. 根据GPL条款, 据称是哥伦比亚大学法学院教授Eben Moglen向Linksys提出了开源要求, Linksys随即照办, 之后在一堆各种hack WRT54G固件中, 2004年生长出来了OpenWrt. 2005年到2007年, 最初的稳定版叫White Russian, 之后的Kamikaze延续到2010年, Backfire到2013年, 随后Attitude Adjustment发布, 而最新版的Barrier Breaker也已经在持续开发中, 据称将很快发布.

从一开始, OpenWrt就是各类路由器hack固件中的领头羊, 并成为嵌入式Linux系统的核心贡献者之一, 特别是Linux on mips, 最近的内核更新代码有很大部分是由OpenWrt社区贡献的.

在各种路由器的hack固件中, OpenWrt为什么能脱颖而出? 笔者认为关键原因是OpenWrt社区彻底的开源精神, 不要忽视<http://openwrt.org>上面明晃晃的"Wireless Freedom"几个字. OpenWrt社区的组织者Gregers Petersen第一title是人类学家, 专注于自由软件及相关社会学研究. 以此为基因, OpenWrt社区聚集了一大批纯正的Linux各个方向的死忠级专家, 从而使OpenWrt具备了如下与传统nor flash嵌入式Linux截然不同的高级特征:

## 1.SquashFS与JFFS2文件系统的整合形成的overlayfs机制

对用户而言, OpenWrt的整个文件系统是完全动态可读写的, 而其中的固件部分是用SquashFS实施的只读压缩文件系统, 而用户所有的对文件系统的增删改都是用类似"差值"的形态存储在JFFS2文件系统中的, 二者用overlayfs机制黏合, 对用户完全透明. 因此我们可以在文件系统中肆意发挥, 随便折腾, 出现任何问题则可像手机一样恢复出厂设置, 并提供fail-safe模式帮助用户修复系统.

而在传统的嵌入式Linux里, 固件是静态的, 对系统做任何一点与可运行程序相关的变动, 比如增加一个模块, 删除一个应用程序, 都要重新编译全部固件, 并重新刷写, 就好比你一个Android手机要升级微信就要重新刷机. 这种反人类的传统文件系统完全阻挡了非专业爱好者进入嵌入式Linux这一领域.

## 2. UCI(Unified Configuration Interface)

帮助用户在任何平台的OpenWrt上用同样的方法配置系统, 网络和应用. 在Boardcom的平台上, 在Atheros的平台上, 甚至x86的平台上, 修改系统配置均为同样的命令. 而UCI的机制并不是二进制硬件虚拟层实现的, 是由Linux shell脚本实现的. 这毫无疑问是一种别致的创新, 比Android来的轻巧得多. OpenWrt里的Linux shell脚本用得很帅很高端, 那种感觉怎么形容呢? 就好像精通十八般武艺的高手有一天特别复古地拿起铅笔刀在硬盘上刻出来了系统, 就是这种感觉.

## 3. Opkg包管理系统与丰富的软件源

是一个与桌面级Linux使用的apt-get, yum等同级别的包管理系统, 使用形如: `opkg install xxxx-app` 的命令从互联网软件源中安装大约3000余种各种软件. 软件数量虽然没法跟手机的应用市场比, 但是要知道, 这里头的任何一个软件都来头不小, 是经过Linux社区千锤百炼的东西, 一个应用折腾一个月都玩不够. 类型覆盖网络, 音频, 视频, 程序开发, Linux系统管理等. 当然, 如果是专业比较偏的东西OpenWrt的软件源里还是不够完善, 比如笔者团队用到的OpenCV的东西, 源里就没有, 就靠自己交叉编译了.

## 4. Luci WEB界面系统

除CLI命令行终端界面外, 不同于桌面级Linux使用屏幕GUI作为交互界面, OpenWrt使用WEB界面交互. 而不同于传统路由器web管理界面的是, luci是用户可订制的, 安装了支持luci的软件后, WEB界面系统就中出现了新的模块, 而opkg本身也web化了.这个特征让用户感觉很像手机的app store.

## 5.积极, 完整的社区

OpenWrt与Arch Linux, Debian, FFmpeg, MinGW, PostgreSQL等开源领域重要的软件一起, 是Software in the Public Interest, Inc.资助和保护的项目, OpenWrt社区在美国, 欧洲, 中国, 俄罗斯有大量的追随者, 有不计其数的分支和代码贡献者. 社区活跃度非常高.

这几个特征加起来, 赋予OpenWrt比肩桌面级Linux和现代移动操作系统(Android)的用户体验, 完全回避了传统嵌入式Linux的磨叽和枯燥, 使一个小小的路由器真正成为完整的, 现代的, 开放的计算系统, 降低了入门门槛, 产生了大量非嵌入式专业的爱好者群体. OpenWrt框架的奠定者们和广泛的代码贡献者们, 在桌面级和现代操作系统的理念下, 也使OpenWrt成为嵌入式Linux领域个性十足而广受追捧的佼佼者.

OpenWrt社区的组织者Gregers Petersen在一次采访中提到, 除了传统的路由器用途, 在智能家居主控设备, 机器人, 飞行器, 工业控制设备, voIP设备等很多领域, 都有爱好者和商业项目在使用OpenWrt, 甚至有爱好者已经完整移植了Android系统并且真正打通了电话. 而嫁接到OpenWrt上的Arduino Yun, 使大家意识到Linux与物理世界交互一种非常简单的可能性, 这赋予了OpenWrt更大的想象空间.

在新型智能设备和机器人的热潮中, OpenWrt的价值也越来越得到人们的重视. 相比Android系统, OpenWrt被认为是更加适应智能设备和机器人的平台. Android的整体设计构架全部着眼于重度依赖屏幕与人进行交互, 导致从硬件到软件的设计上都严重依赖于图形界面的展示, 有过多的GPU硬件加速和软件上的图形, 3D库, 而智能设备和机器人并不强调屏幕, 相对更多地依赖于机械, 网络与人进行交互, Android上的这些图形图像特征反倒成为影响功耗, 系统尺寸, 稳定性的负面因素. 再加之相对于Android的Java虚拟机对效率的严重损耗, OpenWrt直接的原生二进制代码得到了更高的计算效率.

在这个重新强调人工智能, 机器学习, 重新重视物理机械交互的新兴智能机器人的时代, 我们有理由相信因为其纯正的Linux味道, 小型化, 亲近物理交互的特征, 身为Linux社区与物理交互的最佳桥梁, OpenWrt会迎来新一轮的发展.

## Refs
* <http://wemaker.cc/322>