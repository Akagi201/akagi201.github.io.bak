+++
title = "Root Nook Simple Touch"
date = "2014-05-31T23:14:24+08:00"
slug = "root-nook-simple-touch"
githubIssuesID = 28

+++

![nookmanager-success](http://akagi201.qiniudn.com/nookmanager-success.jpg)

今天断网了大半天, 然后玩了一会Calibre, 翻出了我的Nook3, 刚好利用这个假期打算把他root掉.

## 使用NookManager进行root

0. 固件升级到官方1.2.1(我的原来是1.1.5的, 如果不升级那么root时会ModManager会安装失败)
1. 下载NookManager.img.
2. 使用dd命令将NookManager.img写入一个空的sd卡中.(我用Mac OS X系统, linux下类似, win下用相应工具)

```
akagi201@akrmbp ~ $ ls /dev/disk*
/dev/disk0   /dev/disk0s1 /dev/disk0s2 /dev/disk0s3 /dev/disk1   /dev/disk1s1
akagi201@akrmbp ~ $ sudo diskutil umount force /dev/disk1s1
Volume (null) on disk1s1 force-unmounted
akagi201@akrmbp ~ $ sudo dd if=/Users/akagi201/Downloads/NookManager.img of=/dev/disk1 bs=1m
64+0 records in
64+0 records out
67108864 bytes transferred in 49.549986 secs (1354367 bytes/sec)
```

3. 关掉Nook的电源, 插入sd卡, 然后开机, 会显示15秒的NookManager的信息.

![nookmanager-start](http://akagi201.qiniudn.com/nookmanager-start.jpg)

4. 选择"No, continue without wireless", 选yes需要刷机之前设备有连过你附近的ap, 才能验证通过.(这个其实可以改进啦)

![nookmanager-wifi](http://akagi201.qiniudn.com/nookmanager-wifi.jpg)

5. 使用NookManager做一次备份! Rescue -> Backup -> Format remaining space on SD card -> Create backup. (需要花费15~45分钟, 最终备份文件大小是几百M)

![nookmanager-backup](http://akagi201.qiniudn.com/nookmanager-backup.jpg)

6. 使用USB线连接电脑和nook, 拷贝NookBackup分区下的backup.full.gz和backup.full.md5到电脑, 最好上传到网盘备份好.

7. Root! 备份之后, Back -> Back -> Main Menu -> Root -> Root my device (然后看到全是成功, 如果不成功说明你用其他方法root过或者没有升级到官方的1.2.1)

![nookmanager-root](http://akagi201.qiniudn.com/nookmanager-root.jpg)

![nookmanager-success](http://akagi201.qiniudn.com/nookmanager-success.jpg)

8. Back -> Exit -> 拔出SD卡 -> 设备自动重启 -> 选择Relaunch. 搞定.

## Refs
* <http://forum.xda-developers.com/showthread.php?t=2040351>
* <http://nookdevs.com/Nook_Simple_Touch/Rooting>