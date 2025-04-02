# 🌀 一、安装 Node.js

[安装教程](../../../nodejs/安装.md) （笔者安装的版本是: v22.14.0）

# 🌀 二、安装 Python

[安装教程](../../../python/安装/index.md) （笔者安装的版本是: 3.12.7）

# 🌀 三、安装 Java

[安装教程](../../../java/安装.md) （笔者安装的版本是: "21.0.6" 2025-01-21 LTS）

# 🌀 四、安装 Android SDK Tools

## 下载并安装

笔者安装的版本是:

```
PS C:\Users\notebook> adb --version
Android Debug Bridge version 1.0.41
Version 35.0.2-12147458
Installed as C:\platform-tools\adb.exe
```

安装步骤：

1. 进入 [https://developer.android.com/tools/releases/platform-tools?hl=zh-cn#downloads](https://developer.android.com/tools/releases/platform-tools?hl=zh-cn#downloads) （若进入失败，可切换成 edge 浏览器。）
2. 选择 `下载适用于 Windows 的 SDK Platform-Tools`，下载软件压缩包。
3. 将压缩包内的 `platform-tools` 文件夹复制到 C 盘的根目录。
4. 在 `系统属性/高级/环境变量/系统变量/Path` 中，新建 `C:\platform-tools` 这个路径。

## 校验安装

在命令行分别输入以下指令，如果都有响应，则表示安装成功：

* `adb version`

# 🌀 五、安装所需的 Python 软件包

```
pip install uiautomator2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install weditor -i https://pypi.tuna.tsinghua.edu.cn/simple
```

# 🌀 六、配置手机

1. 启用开发者选项。
2. 在开发者选项中，启用 `USB调试`、`USB安装`、`USB调试（安全设置）` 。
3. 使用 usb 连接线将手机连接至电脑。
4. 在命令行执行 `adb devices`，然后在手机弹出的 `允许USB调试吗？` 中选择 `允许` 。
5. 在命令行执行 `adb devices`，查看并记住手机的设备码，后面会用到。

# 🌀 七、测试

运行以下脚本，若手机自动启动微信 APP，则说明安装成功。

[start_wechat.py](start_wechat.py)

# 🌀 八、使用辅助工具

在命令行执行 `weditor` ，在自动打开的网页中，输入设备码，点击 `Connect` 。
