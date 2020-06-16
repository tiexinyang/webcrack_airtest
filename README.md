WEBCRACK_AIRTEST
======

结合Chrome浏览器，一键式爆破网站登录页面，只需提供网站登录目标地址即可
* python only
* Windows下使用AirtestIDE v1.2.3测试通过

安装和依赖
-------------

	1、AirtestIDE (官网下载: http://airtest.netease.com/)
	2、Windows

    
使用
-------------

打开Airtest IDE并导入该项目
编辑config.ini,定义:
* login_url: 攻击目标网站登录页面URL
* enable_dic: 是否启用字典爆破 (True 或 False)
* user_file: 用户字典文件 (默认users.txt)
* pass_file: 密码字典文件 (默认pass.txt) 


原理
-------------

通过Airtest IDE作为辅助,结合Chrome浏览器进行可视化爆破,避免一些常见的cookie/header反破解机制
使用正则自动识别网页用户名/密码输入框,引用基础SQL注入语句以及常见弱口令组合循环遍历,尝试登录
登录成功的判断准则为: 页面不再出现用户名/密码输入框即认为爆破成功
