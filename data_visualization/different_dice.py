# -*- coding: utf-8 -*- 

from die import Die

import pygal

#  ����һ��D6��һ��D10
die_1=Die()
die_2=Die(10)

results=[]
 # ��ɫ�Ӳ�������洢��һ���б���
for roll_num in range(50000):
	result=die_1.roll()+die_2.roll()
	results.append(result)
	# �������
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
	frequency=results.count(value)
	frequencies.append(frequency)
	
# �����ݽ��п��ӻ�
hist=pygal.Bar()

hist.title="Result of rolling two D6 1000 times."
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title="Results"
hist.y_title="Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('different_dice_visual.svg')
