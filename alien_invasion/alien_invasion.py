# -*- coding: utf-8 -*- 

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from introduce import Introduce


def run_game():
    # ��ʼ����Ϸ������һ����Ļ���� 
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#������Ϸ����
	game_introduce= Introduce(ai_settings,screen,"Upper is your score and game level")
	
	#  ����һ��Play��ť
	play_button=Button(ai_settings,screen,"Play")
	
	# ����һ�����ڴ�����Ϸͳ����Ϣ��ʵ��
	stats=GameStats(ai_settings)
	
	# �����洢��Ϸͳ����Ϣ��ʵ���������Ƿ���
	sb=Scoreboard(ai_settings,screen,stats)
	
	#  �����ɴ� 
	ship=Ship(ai_settings,screen)
    
    # ����һ�����ڴ����ӵ��ı���
	bullets=Group()
  
	
    # ����һ�������˱���
	aliens=Group()
    # ����������Ⱥ
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
    # ���ñ���ɫ
	bg_color=(255,228,196)
    
    # ����һ��������
	alien=Alien(ai_settings,screen)
	
    # ��ʼ��Ϸ����ѭ��
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
		
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button,game_introduce)
        
run_game()
