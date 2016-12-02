+++
date = "2016-12-02T10:39:50+08:00"
title = "HTML5 直播协议之 WebSocket 和 MSE"
slug = "websocket-mse"

+++

当前为了满足比较火热的移动 Web 端直播需求, 一系列的 HTML5 直播技术迅速的发展了起来.

常见的可用于 HTML5 的直播技术有 HLS, WebSocket 与 WebRTC. 今天我要向大家介绍一下 WebSocket 与 MSE 相关的内容, 并在最后通过一个实际的例子, 来展示其具体的用法.

## 大纲

* WebSocket 协议介绍.
* WebSocket Client/Server API 介绍.
* MSE 介绍.
* fMP4 介绍.
* Demo 展示.

## WebSocket

通常的 Web 应用都是围绕着 HTTP 的请求/响应模型而构建的. 所有的 HTTP 通信都是通过客户端来控制的, 都是由客户端向服务器发出一个请求, 服务器接收和处理完毕后再返回结果给客户端, 客户端再将数据展现出来. 这种模式不能满足实时应用的需求, 于是出现了 SSE, Comet 等 "服务器推" 的长连接技术.

WebSocket 是直接基于 TCP 连接之上的通信协议, 可以在单个 TCP 连接上进行全双工的通信. WebSocket 在 2011 年被 IETF 定为标准 RFC 6455, 并被 RFC 7936 所补充规范, WebSocket API 被 W3C 定为标准.

WebSocket 是独立的创建在 TCP 上的协议, HTTP 协议中的那些概念都不复存在, 和 HTTP 的唯一关联是使用 HTTP 协议的 101 状态码进行协议切换, 使用的 TCP 端口是 80, 可以用于绕过大多数防火墙的限制.

![websocket_protocol](http://akshare.b0.upaiyun.com/assets/websocket_protocol.png)

### WebSocket 握手

为了更方便地部署新协议，HTTP/1.1 引入了 Upgrade 机制, 它使得客户端和服务端之间可以借助已有的 HTTP 语法升级到其它协议. 这个机制在 RFC7230 的 [6.7 Upgrade](http://httpwg.org/specs/rfc7230.html#header.upgrade)) 一节中有详细描述.

要发起 HTTP/1.1 协议升级，客户端必须在请求头部中指定这两个字段:

```
Connection: Upgrade
Upgrade: protocol-name[/protocol-version]
```
如果服务端同意升级, 那么需要这样响应:

```
HTTP/1.1 101 Switching Protocols
Connection: upgrade
Upgrade: protocol-name[/protocol-version]

[... data defined by new protocol ...]
```

可以看到, HTTP Upgrade 响应的状态码是 `101`, 并且响应正文可以使用新协议定义的数据格式.

WebSocket 握手就利用了这种 HTTP Upgrade 机制. 一旦握手完成，后续数据传输就直接在 TCP 上完成.

### WebSocket JavaScript API

目前主流的浏览器提供了 WebSocket 的 API 接口, 可以发送消息(文本或者二进制)给服务器, 并且接收事件驱动的响应数据.

Step1 检查浏览器是否支持 WebSocket.

```
if(window.WebSocket) {
	// WebSocket代码
}
```

Step2 建立连接

```
var ws = new WebSocket('ws://localhost:8327');
```

Step3 注册回调函数以及收发数据

分别注册 WebSocket 对象的 onopen, onclose, onerror 以及 onmessage 回调函数.

通过 `ws.send()` 来进行发送数据, 这里不仅可以发送字符串, 也可以发送 Blob 或 ArrayBuffer 类型的数据.

如果接收的是二进制数据，需要将连接对象的格式设为 blob 或 arraybuffer.

```
ws.binaryType = 'arraybuffer';
```

### WebSocket Golang API

服务器端 WebSocket 库我推荐使用 Google 自己的 [`golang.org/x/net/websocket`](https://godoc.org/golang.org/x/net/websocket), 可以非常方便的与 `net/http` 一起使用.

可以将 websocket 的 handler function 通过 `websocket.Handler` 转换成 `http.Handler`, 这样就可以跟 `net/http` 库一起使用了.

然后通过 `websocket.Message.Receive` 来接收数据, 通过 `websocket.Message.Send` 来发送数据.

具体代码可以看下面的 Demo 部分.

## MSE

在介绍 MSE 之前, 我们先看看 HTML5 `<audio>` 和 `<video>` 有哪些限制.

### HTML5 <audio> 和 <video> 标签的限制
* 不支持流.
* 不支持 DRM 和加密.
* 很难自定义控制, 以及保持跨浏览器的一致性.
* 编解码和封装在不同浏览器支持不同.

MSE 是解决 HTML5 的流问题.

Media Source Extensions (MSE) 是一个主流浏览器支持的新的 Web API. MSE 是一个 W3C 标准, 允许 JavaScript 动态的构建 `<video>` 和 `<audio>` 的媒体流. 他定义了对象, 允许 JavaScript 传输媒体流片段到一个 HTMLMediaElement.

通过使用 MSE, 你可以动态地修改媒体流而不需要任何的插件. 这让前端 JavaScript 可以做更多的事情, 我们可以在 JavaScript 进行转封装, 处理, 甚至转码.

虽然 MSE 不能让流直接传输到 media tags 上, 但是 MSE 提供了构建跨浏览器播放器的核心技术, 让浏览器通过 JavaScript API 来推音视频到 media tags 上.

现在每个客户端平台都开始逐步开放流媒体相关的 API: Flash 平台有 Netstream, Android 平台有 Media Codec API, 而 Web 上对应的就是标准的 MSE. 由此可以看出, 未来的趋势是在客户端可以做越来越多的事情.

### Browser Support

通过 [caniuse](http://caniuse.com/#feat=mediasource) 来检查是否浏览器支持情况.

![mse-support](http://akshare.b0.upaiyun.com/assets/mse-support.png)

通过 [`MediaSource.isTypeSupported()`](https://developer.mozilla.org/en-US/docs/Web/API/MediaSource/isTypeSupported) 可以进一步地检查 codec MIME 类型是否支持.

比较常用的视频封装格式有 webm 和 fMP4.

WebM 和 WebP 是两个姊妹项目, 都是由 Google 赞助的. 由于 WebM 是基于 Matroska 的容器格式, 所以天生是流式的, 很适合用在流媒体领域里.

下面着重介绍一些 fMP4 格式.

我们都知道 MP4 是由一系列的 Boxes 组成的. 普通的 MP4 的是嵌套结构的, 客户端必须要从头加载一个 MP4 文件, 才能够完整播放, 不能从中间一段开始播放.

而 fMP4 由一系列的片段组成, 如果你的服务器支持 byte-range 请求, 那么, 这些片段可以独立的进行请求到客户端进行播放, 而不需要加载整个文件.

为了更加形象的说明这一点, 下面我介绍几个常用的分析 MP4 文件的工具.

* [gpac](https://gpac.wp.mines-telecom.fr/) 原名 mp4box, 是一个媒体开发框架, 在其源码下有大量的媒体分析工具可以使用, [testapps](https://github.com/gpac/gpac/tree/master/applications/testapps)
* [mp4box.js](http://download.tsi.telecom-paristech.fr/gpac/mp4box.js/filereader.html) 是 mp4box 的 Javascript 版本.
* [bento4](https://www.bento4.com/) 一个专门用于 MP4 的分析工具.
* [mp4parser](http://mp4parser.com/) 在线 MP4 文件分析工具.

### fragment mp4 vs non-fragment mp4

下面一个 fragment mp4 文件通过 [mp4parser](http://mp4parser.com/) 分析后的截图

![fmp4](http://akshare.b0.upaiyun.com/assets/fmp4.png)

下面一个 non-fragment mp4 文件通过 [mp4parser](http://mp4parser.com/) 分析后的截图

![nfmp4](http://akshare.b0.upaiyun.com/assets/nfmp4.png)

Apple 在今年的 WWDC 大会上宣布会在 iOS 10, tvOS, macOS 的 HLS 中支持 fMP4.

值得一提的是, fMP4, CMAF, ISOBMFF 其实都是类似的东西.

### MSE JavaScript API

从高层次上看, MSE 提供了
* 一套 JavaScript API 来构建 media streams.
* 一个拼接和缓存模型.
* 识别一些 byte 流类型:
  * WebM
  * ISO Base Media File Format
  * MPEG-2 Transport Streams

### MSE 内部结构

![mse_arch](http://akshare.b0.upaiyun.com/assets/mse_arch.png)

MSE 本身的设计是不依赖任务特定的编解码和容器格式的, 但是不同的浏览器支持程度是不一样的. 可以通过传递一个 MIME 类型的字符串到静态方法: MediaSource.isTypeSupported 来检查.

比如:

```
MediaSource.isTypeSupported('audio/mp3'); // false
MediaSource.isTypeSupported('video/mp4'); // true
MediaSource.isTypeSupported('video/mp4; codecs="avc1.4D4028, mp4a.40.2"'); // true
```

获取 Codec MIME string 的方法可以通过在线的 [mp4info](http://nickdesaulniers.github.io/mp4info/) 或者使用命令行 `mp4info test.mp4 | grep Codecs`

可以得到类似如下结果:

```
❯ mp4info fmp4.mp4| grep Codec
    Codecs String: mp4a.40.2
    Codecs String: avc1.42E01E
```

当前, H.264 + AAC 的 MP4 容器在所有的浏览器都支持.

普通的 MP4 文件是不能和 MSE 一起使用的, 需要将 MP4 进行 fragment 化.

检查一个 MP4 是否已经 fragment 的方法

```
mp4dump test.mp4 | grep "\[m"
```

如果是 non-fragment 会显示类似信息.

```
❯ mp4dump nfmp4.mp4 | grep "\[m"
[mdat] size=8+50873
[moov] size=8+7804
  [mvhd] size=12+96
    [mdia] size=8+3335
      [mdhd] size=12+20
      [minf] size=8+3250
    [mdia] size=8+3975
      [mdhd] size=12+20
      [minf] size=8+3890
            [mp4a] size=8+82
    [meta] size=12+78
```

如果已经 fragment, 会显示如下类似信息.

```
❯ mp4dump fmp4.mp4 | grep "\[m" | head -n 30
[moov] size=8+1871
  [mvhd] size=12+96
    [mdia] size=8+312
      [mdhd] size=12+20
      [minf] size=8+219
            [mp4a] size=8+67
    [mdia] size=8+371
      [mdhd] size=12+20
      [minf] size=8+278
    [mdia] size=8+248
      [mdhd] size=12+20
      [minf] size=8+156
    [mdia] size=8+248
      [mdhd] size=12+20
      [minf] size=8+156
  [mvex] size=8+144
    [mehd] size=12+4
[moof] size=8+600
  [mfhd] size=12+4
[mdat] size=8+138679
[moof] size=8+536
  [mfhd] size=12+4
[mdat] size=8+24490
[moof] size=8+592
  [mfhd] size=12+4
[mdat] size=8+14444
[moof] size=8+312
  [mfhd] size=12+4
[mdat] size=8+1840
[moof] size=8+600
```

把一个 non-fragment MP4 转换成 fragment MP4.

可以使用 FFmpeg 的 `-movflags` 来转换

对于原始文件为非 MP4 文件

```
ffmpeg -i trailer_1080p.mov -c:v copy -c:a copy -movflags frag_keyframe+empty_moov bunny_fragmented.mp4
```

对于原始文件已经是 MP4 文件

```
ffmpeg -i non_fragmented.mp4 -movflags frag_keyframe+empty_moov fragmented.mp4
```

或者使用 mp4fragment

```
mp4fragment input.mp4 output.mp4
```

## demo

* [MSE Vod Demo](https://github.com/Akagi201/learning-webrtc/tree/master/mse/vod) 展示利用 MSE 和 WebSocket 实现一个点播服务.
* [MSE Live Demo](https://github.com/Akagi201/learning-webrtc/tree/master/mse/live) 展示利用 MSE 和 WebSocket 实现一个直播服务.

## MSE VOD Demo

<video src="http://akshare.b0.upaiyun.com/assets/mse_vod_demo.mp4" controls="controls">
Your browser does not support the video tag.
</video>

## MSE Live Demo

<video src="http://akshare.b0.upaiyun.com/assets/mse_live_demo.mp4" controls="controls">
Your browser does not support the video tag.
</video>

## Refs
### WebSocket
* [rfc6455](https://tools.ietf.org/html/rfc6455)
* [HTTP Upgrade](https://imququ.com/post/protocol-negotiation-in-http2.html)
* [WebSocket API](http://javascript.ruanyifeng.com/htmlapi/websocket.html)
* [MDN WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
* [videojs-flow](https://github.com/winlinvip/videojs-flow)

### MSE
* [W3C](https://www.w3.org/TR/media-source)
* [MDN MSE](https://developer.mozilla.org/en-US/docs/Web/API/MediaSource)
* [HTML5 Codec MIME](http://www.leanbackplayer.com/test/h5mt.html)
