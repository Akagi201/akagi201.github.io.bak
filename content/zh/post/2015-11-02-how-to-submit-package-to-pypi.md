+++
date = "2015-11-02T09:59:54+08:00"
title = "如何提交Package到PyPI"
slug = "how-to-submit-package-to-pypi"

+++

## PyPI官方文档
* <https://pypi.python.org/pypi>
* <https://wiki.python.org/moin/CheeseShopTutorial#Submitting_Packages_to_the_Package_Index>

## Steps
### 注册账号
* PyPI Live <https://pypi.python.org/pypi?%3Aaction=register_form>
* PyPI Test <https://testpypi.python.org/pypi?%3Aaction=register_form>

### 填写配置文件`~/.pypirc`

```
[distutils]
index-servers=
    pypi
    pypitest

[pypitest]
repository = https://testpypi.python.org/pypi
username = <your user name goes here>
password = <your password goes here>

[pypi]
repository = https://pypi.python.org/pypi
username = <your user name goes here>
password = <your password goes here>
```

### 准备你的package

PyPI上的每个package需要一个`setup.py`文件在项目的根目录, 如果你在一个一个markdown格式的README文件, 你还需要一个`setup.cfg`文件. 一个`LICENSE.txt`文件. 假设包名为:`mypackage`, 目录结构如下.

```
├── LICENSE.txt
├── README.md
├── mypackage
│   ├── __init__.py
│   ├── bar.py
│   ├── baz.py
│   └── foo.py
├── setup.cfg
└── setup.py
```

#### `setup.py`

```
from distutils.core import setup

setup(
    name='mypackage',
    packages=['mypackage'],  # this must be the same as the name above
    version='0.1',
    description='A random test lib',
    author='Akagi201',
    author_email='akagi201@gmail.com',
    url='https://github.com/Akagi201/mypackage',  # use the URL to the github repo
    download_url='https://github.com/Akagi201/mypackage/tarball/0.1',  # I'll explain this in a second
    keywords=['testing', 'logging', 'example'],  # arbitrary keywords
    classifiers=[],
)
```

`download_url`: repo源码的下载链接, 使用`git tag`后, github会为你host. 使用命令: `git tag 0.1 -m "Adds a tag so that we can put this on PyPI."`, 使用 `git push --tags origin master` 提交到github

#### `setup.cfg`

告诉PyPI你的README文件的位置.

```
[metadata]
description-file = README.md
```

### 提交package到PyPI Test
* 注册: `python setup.py register -r pypitest`
* 上传: `python setup.py sdist upload -r pypitest`
* 安装: `pip install -i https://testpypi.python.org/pypi <package name>`

### 提交package到PyPI Live
* 注册: `python setup.py register -r pypi`
* 上传: `python setup.py sdist upload -r pypi`
* web form提交: `https://pypi.python.org/pypi?:action=submit_form`

## 不使用`setuptools`, 使用更安全的`twine`上传
* `twine upload dist/*`

## Refs
* <http://peterdowns.com/posts/first-time-with-pypi.html>
* <https://packaging.python.org/en/latest/distributing/#uploading-your-project-to-pypi>
* <http://pythonhosted.org/an_example_pypi_project/>
* <https://wiki.python.org/moin/TestPyPI>
* 较新: <https://packaging.python.org/en/latest/current/>
* <https://pypi.python.org/pypi?%3Aaction=list_classifiers>
* <https://coderwall.com/p/qawuyq/use-markdown-readme-s-in-python-modules>
* <http://python-packaging-user-guide.readthedocs.org/en/latest/single_source_version/>
