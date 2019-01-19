# -*- coding: utf-8 -*- 

from die import Die

import pygal

#  创建一个D6和一个D10
die_1=Die()
die_2=Die(10)

results=[]
 # 掷色子并将结果存储在一个列表中
for roll_num in range(50000):
	result=die_1.roll()+die_2.roll()
	results.append(result)
	# 分析结果
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
	frequency=results.count(value)
	frequencies.append(frequency)
	
# 对数据进行可视化
hist=pygal.Bar()

hist.title="Result of rolling two D6 1000 times."
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title="Results"
hist.y_title="Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('different_dice_visual.svg')
