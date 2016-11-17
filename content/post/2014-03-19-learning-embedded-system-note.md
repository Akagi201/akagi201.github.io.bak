+++
title = "Learning Embedded System Note"
date = "2014-03-09T13:41:47+08:00"
slug = "learning-embedded-system-note"

+++

<iframe src="https://atlas.mindmup.com/akagi201/sundy_android_low_level/index.html" height="100%" width = "100%"></iframe>

换工作这几个月的时间, 还是挺爽的, 时间完全自由支配. 把之前因为工作比较忙的原因没空学习的东西都恶补了一下, 这几个月太赞了, 积累了不少资源, 把openwrt玩遍了, 将ARM-linux嵌入式完整的学习了一遍, 并用思维导图做了笔记. 

## 精华部分
* 应用层所有的东西包括系统调用, C库, pthread库, socket等等全都在glibc的官方文档里面了<http://www.gnu.org/software/libc/manual/>.
* 很多东西linux和android是相通的, 很多android的东西已经融入到了底层驱动中. 所以, 小米有android的深厚技术基础来发展linux, 相当easy.
* 思维导图是个好东西, 用来索引记忆还是不错的. 长篇大论还是去别的地方找好了, 没必要记录太多东西. 
* ARM交叉编译工具链下载地址 <http://www.linaro.org/>

## RTC驱动框图

学习了一种工具画流程图工具.

<iframe id="embed_dom" name="embed_dom" frameborder="0" style="border:1px solid #000;display:block;width:430px; height:320px;" src="http://www.processon.com/embed/532d8ae60cf253b242881338"></iframe>