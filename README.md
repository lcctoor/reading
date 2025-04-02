# 描述

一个文本离线朗读软件。用户既可以在界面上输入文本进行朗读，也能选择本地的文本文件进行全文朗读。

# 作者

作者: 许灿标

链接: [主页](https://lcctoor.com) \| [Github](https://github.com/lcctoor) \| [PyPi](https://pypi.org/user/lcctoor) \| [微信](https://lcctoor.com/cdn/WeChatQRC.jpg) \| [邮箱](mailto:lcctoor@outlook.com) \| [捐赠](https://lcctoor.com/cdn/DonationQRC-0rmb.jpg)

# 教程

## 安装

```
pip install reading
```

## 运行

```python
from reading import reading_server

reading_server(port=9355)  # 可通过 port 参数指定服务端口
```

此时, 将自动打开浏览器, 并访问 `http://localhost:9355/` .
