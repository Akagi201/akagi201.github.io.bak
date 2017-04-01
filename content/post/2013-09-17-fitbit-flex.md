+++
title = "Fitbit Flex"
date = "2013-09-17T14:32:08+08:00"
slug = "fitbit-flex"
githubIssuesID = 3

+++


* 排斥英文的小伙伴们可以不用看了, 各种数据, 各种软件全是英文的.
## clients
* pc: http://www.fitbit.com/setup 下载安装 FitbitConnect, 貌似只有2个功能: 同步和升级固件.第一次使用会搜索设备, 然后搜到之后, 双击一下手环表示确认, 我勒个去, 太有科技感了.看配置信息(dashboard)会跳转到网页.
* Android: 只能看数据, 同步目前需要蓝牙4.0, wifi现在还不支持, 看fitbit的开发博客貌似正在beta阶段.

## update firmware
* 通过pc端可以升级, 刚入手时候是50, 升级后变成64了. 具体多了哪些功能还不清楚, 总之越新越好. 升级过程有点慢, 手都不敢动, 很怕升级失败的说.

## Specs
* 5个白点LED灯，一个蓝牙芯片，一个三轴加速度传感器，一个振动马达，还有一个主控芯片，微小的电池续航能力竟能达到5-7天。还有一块NFC标签, 用于支持NFC的手机同步的.
* 五个LED灯是跟天线套在一个塑料壳上，有一层黑色胶布把它、电池和整块电路板绑在一起，合得比较紧密.
* 蓝牙芯片使用的是Nordic的NRF8001.
* 接下来有两片不明的芯片写有“NXE”和“NAI”字样，其中NAI芯片上还带有疑似二维码的信息.
* 主控芯片用的是意法半导体的STM32L。电池容量未标清，目测可能是20mAh左右.

## 关于卡路里消耗的精度问题
* 由于fitbit有庞大的数据库源，只要你输入了精确的身高+体重，fitbit就能基本了解你的步长和单步消耗卡路里的平均值，之后这些数据都会很准。 
* 所以初次使用，建议录入自己的精确身高和体重，以后记得更新体重的变化，这样会让数据更准。

## 睡眠跟踪
* 睡前 拍打4-5下触发睡眠跟踪模式，早上醒来再同样操作即可。 在刚躺下的时候记得猛拍它，进入睡眠模式，这样早晨sync一下就能以图表的形式看到昨晚睡眠情况，中途醒了几次，深度睡眠浅度睡眠分别占了多少。我觉得一天几个小时就差不多了，再多真是挥霍生命。

## 充电
* 大概半小时就能冲到8成以上，但是足足充满需要两三小时的，充满电五颗LED会同时闪烁.

## 操作
* 没有任何可见的按钮，平时的操作是靠快速点击：啪啪两下，显示今日目标完成情况，5颗LED各代表20%完成度。。如果猛烈的啪啪啪啪啪点了好多下，就会进入睡眠模式，最左和最右两颗LED亮，再一次啪啪啪啪啪就会切回普通计步模式。而且LED绝大部分时候也是不会亮的，据说运动量达到了设定的目标会有震动和”happy dancing”

## Refs
* <http://www.leiphone.com/chaijie-fitbit-flex.html>
* <https://help.fitbit.com/customer/portal/articles/798019>
* <http://tech2ipo.com/59590>
* <http://knewone.com/things/fitbit-flex/reviews/51af49127373c295b700001c>
* <https://zlz.im/fitbit-flex-review/>
* [Fitbit 官方中文小组](http://www.fitbit.com/group/229BXW)
* [Fitbit API](http://dev.fitbit.com/)
* [Fitbit 豆瓣小组](http://www.douban.com/group/fitbit/)