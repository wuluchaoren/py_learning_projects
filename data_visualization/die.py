# -*- coding: utf-8 -*- 

from random import randint

class Die():
	# ����һ��ɫ����
	def __init__(self,num_sides=6):
		# ɫ��Ĭ��������
		self.num_sides=num_sides
		
	def roll(self):
		# ����һ��λ��1������֮������ֵ
		return randint(1,self.num_sides)
