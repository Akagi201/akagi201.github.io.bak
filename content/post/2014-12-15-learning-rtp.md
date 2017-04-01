+++
title = "Learning RTP"
date = "2014-12-15T21:50:26+08:00"
slug = "learning-rtp"
githubIssuesID = 43

+++

<iframe src="https://atlas.mindmup.com/akagi201/learning_rtp/index.html" height="100%" width = "100%"></iframe>

`RTP`(Real-time Transport Protocol)是用于Internet上针对多媒体数据流的一种传输协议. `RTP`被定义为在一对一或一对多的传输情况下工作, 其目的是提供时间信息和实现流同步. `RTP`通常使用`UDP`来传送数据, 但`RTP`也可以在`TCP`或`ATM`等其他协议之上工作.

`RTP`本身并没有提供按时发送机制或其他服务质量(QoS)保证, 它依赖于底层服务去实现这一过程. `RTP`并不保证传送或防止无序传送, 也不确定底层网络的可靠性.

## book
* <https://www.safaribooksonline.com/library/view/rtp-audio-and/0672322498/>
* <http://www.amazon.com/RTP-Audio-Video-Internet-paperback/dp/0321833627>
