# -*- coding: utf-8 -*- 

from random import randint

class Die():
	# 定义一个色子类
	def __init__(self,num_sides=6):
		# 色子默认六个面
		self.num_sides=num_sides
		
	def roll(self):
		# 返回一个位于1和面数之间的随机值
		return randint(1,self.num_sides)
