# 连接服务器

ssh root@119.45.120.97

# 从本地传文件到远程服务器

以下方法只能传文件, 不能传文件夹:

```
scp C:\文件夹\文件.zip root@123.123.123.123:/文件夹/文件.zip
```

# 解决SSH连接长时间不操作自动断开

1. 修改/etc/ssh/sshd_config文件

```
ClientAliveInterval 60  # 表示每60秒发送一次, 然后客户端响应, 这样就保持长连接了.
ClientAliveCountMax 10  # 表示服务器发出请求后客户端没有响应的次数达到一定值, 就自动断开，正常情况下, 客户端不会不响应.
```

2. 重启sshd服务

```
service sshd restart # 或者 service ssh restart
```

