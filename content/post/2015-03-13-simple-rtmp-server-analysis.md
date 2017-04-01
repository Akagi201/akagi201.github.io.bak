+++
title = "Simple RTMP Server分析"
date = "2015-03-13T08:24:08+08:00"
slug = "simple-rtmp-server-analysis"
githubIssuesID = 50

+++

## 源码目录分析

* 整体目录

```
.
├── 3rdparty/ # 第三方库源码跟补丁
├── Makefile  # 通过configure生成的Makefile
├── auto/     # configure读取执行特定功能的脚本
├── conf/     # srs启动的配置文件*.conf
├── configure # 编译脚本用于根据用户参数生成Makefile跟.h文件
├── doc/      # 协议RFC
├── etc/      # linux启动脚本
├── ide/      # IDE工程文件
├── modules/  # 目前为空
├── objs/     # 编译结果
├── research/ # 预研项目
├── scripts/  # 辅助脚本
└── src/      # 源码
```

* 源码目录

```
.
├── app
│   ├── srs_app_bandwidth.cpp
│   ├── srs_app_bandwidth.hpp
│   ├── srs_app_config.cpp
│   ├── srs_app_config.hpp
│   ├── srs_app_conn.cpp
│   ├── srs_app_conn.hpp
│   ├── srs_app_dvr.cpp
│   ├── srs_app_dvr.hpp
│   ├── srs_app_edge.cpp
│   ├── srs_app_edge.hpp
│   ├── srs_app_empty.cpp
│   ├── srs_app_empty.hpp
│   ├── srs_app_encoder.cpp
│   ├── srs_app_encoder.hpp
│   ├── srs_app_ffmpeg.cpp
│   ├── srs_app_ffmpeg.hpp
│   ├── srs_app_forward.cpp
│   ├── srs_app_forward.hpp
│   ├── srs_app_hds.cpp
│   ├── srs_app_hds.hpp
│   ├── srs_app_heartbeat.cpp
│   ├── srs_app_heartbeat.hpp
│   ├── srs_app_hls.cpp
│   ├── srs_app_hls.hpp
│   ├── srs_app_http.cpp
│   ├── srs_app_http.hpp
│   ├── srs_app_http_api.cpp
│   ├── srs_app_http_api.hpp
│   ├── srs_app_http_client.cpp
│   ├── srs_app_http_client.hpp
│   ├── srs_app_http_conn.cpp
│   ├── srs_app_http_conn.hpp
│   ├── srs_app_http_hooks.cpp
│   ├── srs_app_http_hooks.hpp
│   ├── srs_app_ingest.cpp
│   ├── srs_app_ingest.hpp
│   ├── srs_app_json.cpp
│   ├── srs_app_json.hpp
│   ├── srs_app_kbps.cpp
│   ├── srs_app_kbps.hpp
│   ├── srs_app_listener.cpp
│   ├── srs_app_listener.hpp
│   ├── srs_app_log.cpp
│   ├── srs_app_log.hpp
│   ├── srs_app_mpegts_udp.cpp
│   ├── srs_app_mpegts_udp.hpp
│   ├── srs_app_pithy_print.cpp
│   ├── srs_app_pithy_print.hpp
│   ├── srs_app_recv_thread.cpp
│   ├── srs_app_recv_thread.hpp
│   ├── srs_app_refer.cpp
│   ├── srs_app_refer.hpp
│   ├── srs_app_reload.cpp
│   ├── srs_app_reload.hpp
│   ├── srs_app_rtmp_conn.cpp
│   ├── srs_app_rtmp_conn.hpp
│   ├── srs_app_rtsp.cpp
│   ├── srs_app_rtsp.hpp
│   ├── srs_app_security.cpp
│   ├── srs_app_security.hpp
│   ├── srs_app_server.cpp
│   ├── srs_app_server.hpp
│   ├── srs_app_source.cpp
│   ├── srs_app_source.hpp
│   ├── srs_app_st.cpp
│   ├── srs_app_st.hpp
│   ├── srs_app_st_socket.cpp
│   ├── srs_app_st_socket.hpp
│   ├── srs_app_statistic.cpp
│   ├── srs_app_statistic.hpp
│   ├── srs_app_thread.cpp
│   ├── srs_app_thread.hpp
│   ├── srs_app_utility.cpp
│   └── srs_app_utility.hpp
├── core
│   ├── srs_core.cpp
│   ├── srs_core.hpp
│   ├── srs_core_autofree.cpp
│   ├── srs_core_autofree.hpp
│   ├── srs_core_performance.cpp
│   └── srs_core_performance.hpp
├── kernel
│   ├── srs_kernel_aac.cpp
│   ├── srs_kernel_aac.hpp
│   ├── srs_kernel_buffer.cpp
│   ├── srs_kernel_buffer.hpp
│   ├── srs_kernel_codec.cpp
│   ├── srs_kernel_codec.hpp
│   ├── srs_kernel_consts.cpp
│   ├── srs_kernel_consts.hpp
│   ├── srs_kernel_error.cpp
│   ├── srs_kernel_error.hpp
│   ├── srs_kernel_file.cpp
│   ├── srs_kernel_file.hpp
│   ├── srs_kernel_flv.cpp
│   ├── srs_kernel_flv.hpp
│   ├── srs_kernel_log.cpp
│   ├── srs_kernel_log.hpp
│   ├── srs_kernel_mp3.cpp
│   ├── srs_kernel_mp3.hpp
│   ├── srs_kernel_stream.cpp
│   ├── srs_kernel_stream.hpp
│   ├── srs_kernel_ts.cpp
│   ├── srs_kernel_ts.hpp
│   ├── srs_kernel_utility.cpp
│   └── srs_kernel_utility.hpp
├── libs
│   ├── srs_lib_bandwidth.cpp
│   ├── srs_lib_bandwidth.hpp
│   ├── srs_lib_simple_socket.cpp
│   ├── srs_lib_simple_socket.hpp
│   ├── srs_librtmp.cpp
│   └── srs_librtmp.hpp
├── main
│   └── srs_main_server.cpp
├── protocol
│   ├── srs_raw_avc.cpp
│   ├── srs_raw_avc.hpp
│   ├── srs_rtmp_amf0.cpp
│   ├── srs_rtmp_amf0.hpp
│   ├── srs_rtmp_buffer.cpp
│   ├── srs_rtmp_buffer.hpp
│   ├── srs_rtmp_handshake.cpp
│   ├── srs_rtmp_handshake.hpp
│   ├── srs_rtmp_io.cpp
│   ├── srs_rtmp_io.hpp
│   ├── srs_rtmp_msg_array.cpp
│   ├── srs_rtmp_msg_array.hpp
│   ├── srs_rtmp_sdk.cpp
│   ├── srs_rtmp_sdk.hpp
│   ├── srs_rtmp_stack.cpp
│   ├── srs_rtmp_stack.hpp
│   ├── srs_rtmp_utility.cpp
│   ├── srs_rtmp_utility.hpp
│   ├── srs_rtsp_stack.cpp
│   └── srs_rtsp_stack.hpp
└── utest
    ├── srs_utest.cpp
    ├── srs_utest.hpp
    ├── srs_utest_amf0.cpp
    ├── srs_utest_amf0.hpp
    ├── srs_utest_config.cpp
    ├── srs_utest_config.hpp
    ├── srs_utest_core.cpp
    ├── srs_utest_core.hpp
    ├── srs_utest_kernel.cpp
    ├── srs_utest_kernel.hpp
    ├── srs_utest_protocol.cpp
    ├── srs_utest_protocol.hpp
    ├── srs_utest_reload.cpp
    └── srs_utest_reload.hpp
```

## 编译脚本分析

### `/trunk/configure`

`configure`是个`Bash`脚本, 根据配置来生成`Makefile`跟`.h`文件.

1. 如果存在`Makefile`文件, 则执行`make clean`
2. 删除`Makefile`
3. 创建`objs`目录
4. 导入并执行`auto/options.sh`用于解析用户的编译参数, 对相应的SRS_XXX的变量进行赋值.
5. 导入`auto/generate-srs-librtmp-project.sh`用于生成srs-librtmp项目, 创建项目目录, 拷贝一些文件到对应目录. `research/librtmp/*.c research/librtmp/Makefile auto/generate_header.sh auto/generate-srs-librtmp-single.sh src/core/* src/kernel/* src/protocol/* src/libs/*`
6. 导入并执行`auto/depends.sh`, 检查缺少的依赖工具并安装
7. 导入并执行`auto/auto_headers.sh`, 生成`srs_auto_headers.hpp`, 声明配置的宏.
8. srs modules相关
9. 编译工具跟编译参数赋值.
10. 指定第三方库路径
11. 调用`auto/modules.sh`将不同模块写入Makefile中.
12. 生成srs app的编译目标的相关的Makefile代码. `auto/apps.sh`
13. 生成utest的编译目标的相关的Makefile代码. `auto/utest.sh`
14. 颜色化输出`auto/summary.sh`
15. 生成`Makefile`

### 导出`srs-librtmp`项目源码与编译
* `./configure --export-librtmp-project=srs-librtmp`
* `cd srs-librtmp && make`
* 成果物: `objs/include/srs_librtmp.h` `objs/lib/srs_librtmp.a`
* examples: `research/librtmp` <https://github.com/winlinvip/simple-rtmp-server/wiki/v2_CN_SrsLibrtmp#srs-librtmp-examples>
* 源码: `src`























