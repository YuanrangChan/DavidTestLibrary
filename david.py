#coding:utf-8
from selenium import webdriver
from time import *

a = int()
b = int()
	
	
class David(object):
	def __init__(self):
		pass
	def jia(self,a,b):
		u"加法"
		return a + b
		
	def jian(self,a,b):
		u"减法"
		return a - b

	def cheng(self,a,b):
		u"乘法"
		return a * b

	def chu(self,a,b):
		u"除法"
		return a / b		
	
	def login(self,username,psw):
		u"这里写了一个登录博客园的方法，账号和密码参数化"
		self.driver = webdriver.Firefox()
		url = "https://passport.cnblogs.com/user/signin"
		self.driver.get(url)
		self.driver.implicitly_wait(30)
		self.driver.find_element_by_id("input1").send_keys(username)
		self.driver.find_element_by_id("input2").send_keys(psw)
		self.driver.find_element_by_id("signin").click()
		sleep(5)
		self.driver.quit()

	def is_login_sucess(self):
		u"判断是否获取到登录账户名称"
		try:
			text = self.driver.find_element_by_id("ink_current_user").text
			print text
			return True
		except:
			return False
