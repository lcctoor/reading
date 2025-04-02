# 安装 Python

## 下载软件包

[https://www.python.org/downloads/](https://www.python.org/downloads/)

## 安装软件

在开始安装前，须先注意以下几点：

1. 选择 `Install Now` 而不是 `Customize installation` 。
2. 安装过程中，所有可选框全部打勾。
3. 如果有看到 `Disable path length limit` ，建议点击该选项。

## 校验安装

在命令行分别输入以下指令，如果都有响应，则表示安装成功：

* `python --version`
* `pip`

## 安装 Microsoft Visual C++(>=14.0)

(若未安装 Microsoft Visual C++(>=14.0) ，将来在安装某些第三方包时可能会失败。)

1. 进入 [https://visualstudio.microsoft.com/zh-hans/downloads/](https://visualstudio.microsoft.com/zh-hans/downloads/) ，下载 Visual Studio 。
2. 运行 Visual Studio 安装包，勾选 `使用 C++ 的桌面开发` ，然后点击安装。

<img src="1.png" width="60%">

## 使用 Unicode UTF-8 提供全球语言支持

(若未启用 Unicode UTF-8 全球语言支持，将来在安装某些第三方包时可能会失败。)

根据这篇教程启用：[https://jingyan.baidu.com/article/64d05a023265439f54f73b00.html](https://jingyan.baidu.com/article/64d05a023265439f54f73b00.html) 。

启用后，最好重启一下电脑。
