# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	rw=RandomWalk(30000)
	rw.fill_walk()
	
	# ÉèÖÃ»æÍ¼´°¿ÚµÄ³ß´ç
	plt.figure(figsize=(10,6))
	
	point_numbers=list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Reds,edgecolor='none',s=5)
	
	plt.scatter(0,0,c='green',edgecolors='none',s=10)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='green',edgecolors='none',s=10)
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	
	keep_running=input("Make another walk?(y/n):")
	if keep_running=='n':
		break
