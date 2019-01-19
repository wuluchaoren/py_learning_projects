# -*- coding: utf-8 -*- 

import pygame.font

class Introduce():
	def __init__(self,ai_settings,screen,msg):
		# ��ʼ�����ܵ�����
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		# ���ý��ܵĳߴ����������
		self.width,self.height=350,50
		self.button_color=255,228,196
		self.text_color=139,139,122
		self.font=pygame.font.SysFont(None,30)
		
		# ������ť��rect����ʹ�����
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.bottom=self.screen_rect.bottom
		self.rect.right=self.screen_rect.right
		
		# ��ť�ı�ǩֻ�贴��һ��
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
		# ��msg��ȾΪͼ��ʹ���ڽ����Ͼ���
		self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center
	
	def draw_button(self):
		# ����һ������ɫ���Ľ����ٻ����ı�
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)

