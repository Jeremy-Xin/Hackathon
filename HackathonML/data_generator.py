from __future__ import division
import pandas as pd
import numpy as np
import random

columns = ['temperature','blood_pressure','heart_rate','breathing_rate', 'vertical_speed', 'horizontal_speed', 'drowning']

for i in range(10000):
	tem = 37 + random.randint(-12, 8) / 10
	bp = 80 + random.randint(0, 60)
	hr = 60 + random.randint(0, 60) + random.randint(0, 9) / 10
	br = random.randint(0, 25) + random.randint(0, 9) / 10
	sp_v = random.randint(0, 3) + random.randint(0, 9) / 10
	sp_h = random.randint(0, 9) / 10
	if sp_v < 2.5 and sp_h > 0.1 and hr > 90 and br < 15 and (bp / (tem - 35)) < 100:
		drowning = True
	else:
		drowning = False
	a = pd.Series({
			'temperature': tem,
			'blood_pressure' : bp,
			'heart_rate': hr,
			'breathing_rate': br,
			'vertical_speed': sp_v,
			'horizontal_speed': sp_h,
			'drowning': drowning
		}, name=str(i), )
	df = df.append(a)
df['drowning'] = df['drowning'].astype('bool')


df.to_csv('data.csv', index=False, sep=',', columns=columns)
