# app_ftp_server

## 安装pyftpdlib
pip3 install pyftpdlib

## 修改 conf/harborftp.conf文件
1. 修改access_key和secret_key： http://obs.casearth.cn/apidocs/ 登录harbor账号后获取。
2. 修改bucket：harbor系统中创建的桶的名字。
3. 修改login_users: 登录ftp的账户和密码，配置格式为<用户名:密码:读写权限>，多个账户用分号分割。

## 运行
python3 harbor_ftp.py

## 使用
1. 安装任意一款ftp客户端即可，服务器地址：yourip:2121，账号密码为配置文件中的login_users。
2. 或者浏览器ftp://yourip:2121 账号密码为配置文件中的login_users。

