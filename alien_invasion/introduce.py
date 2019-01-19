# -*- coding: utf-8 -*- 

import pygame.font

class Introduce():
	def __init__(self,ai_settings,screen,msg):
		# 初始化介绍的属性
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		# 设置介绍的尺寸和其他属性
		self.width,self.height=350,50
		self.button_color=255,228,196
		self.text_color=139,139,122
		self.font=pygame.font.SysFont(None,30)
		
		# 创建按钮的rect对象并使其居中
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.bottom=self.screen_rect.bottom
		self.rect.right=self.screen_rect.right
		
		# 按钮的标签只需创建一次
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
		# 将msg渲染为图像并使其在介绍上居中
		self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center
	
	def draw_button(self):
		# 绘制一个用颜色填充的介绍再绘制文本
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)

