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
