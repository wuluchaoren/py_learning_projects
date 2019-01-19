# -*- coding: utf-8 -*- 

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		# ��ʼ�������˲���ʼ��λ��
		super(Alien,self).__init__()
		self.screen=screen
		self.ai_settings=ai_settings
		
		# ����������ͼ��
		self.image=pygame.image.load('images/alien2.bmp')
		self.rect=self.image.get_rect()
		
		# ÿ�����������������Ļ���ϽǸ���
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		
		# ���������˵�׼ȷλ��
		self.x=float(self.rect.x)
		
	def blitme(self):
		# ��ָ��λ�û���������
		self.screen.blit(self.image,self.rect)
		
	def update(self):
		# �ƶ�������
		self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
		self.rect.x=self.x
	
	def check_edges(self):
		# ���������λ����Ļ��Ե�ͷ���True
		screen_rect=self.screen.get_rect()
		if self.rect.right>=screen_rect.right:
			return True
		elif self.rect.left<=0:
			return True
