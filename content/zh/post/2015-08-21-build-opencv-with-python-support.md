+++
title = "Build OpenCV With Python Support"
date = "2015-08-21T06:43:26+08:00"
slug = "buid-opencv-with-python-support"

+++

## steps
1. Download `opencv-2.4.11.zip` from <http://opencv.org/downloads.html>
2. `unzip opencv-2.4.11.zip`
3. `cd opencv-2.4.11`
4. `mkdir release`
5. `cd release`
6. `export PYTHONPATH="/path_to_python/lib/python2.6/site-packages/:$PYTHONPATH"`
7. `cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_PYTHON_SUPPORT=ON ..`
8. 如果上一步找不到python相关路径, `ccmake ..`, 然后手动指定 PYTHON_PACKAGES_PATH, PYTHON_EXECUTABLE, PYTHON_INCLUDE_DIR, PYTHON_LIBRARY, PYTHON_PACKAGES_PATH 这几个变量的位置.
```
PYTHON_EXECUTABLE="/path_to_python/bin/python"
PYTHON_INCLUDE_DIR="/path_to_python/include/python2.6"
PYTHON_LIBRARY="/path_to_python/lib/python2.6/config/libpython2.6.a"
PYTHON_PACKAGES_PATH="/path_to_python/lib/python2.6/site-package"
```
9. `make`
10. `sudo make install`

## test
1. `python`
2. `import cv2`

## Refs
* <http://docs.opencv.org/doc/tutorials/introduction/linux_install/linux_install.html>