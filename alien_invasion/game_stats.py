# -*- coding: utf-8 -*- 

class GameStats():
	# ������Ϸ��ͳ����Ϣ
	def __init__(self,ai_settings):
		# ��ʼ��ͳ����Ϣ
		self.ai_settings=ai_settings
		self.reset_stats()
		# ����Ϸһ��ʼ���ڷǻ״̬
		self.game_active=False
		# �κ�����¶���Ӧ��������ߵ÷�
		self.high_score=0
		
	def reset_stats(self):
		# ��ʼ������Ϸ�����ڼ���ܱ仯��ͳ����ʾ
		self.ships_left=self.ai_settings.ship_limit
		self.score=0
		self.level=1
		
