# -*- coding: utf-8 -*- 

import pygal

from die import Die 

#   创建两个D6色子
die_1=Die()
die_2=Die()

results=[]
 # 掷色子并将结果存储在一个列表中
for roll_num in range(1000):
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
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title="Results"
hist.y_title="Frequency of Result"

hist.add('D6+D6',frequencies)
hist.render_to_file('dice_visual.svg')
