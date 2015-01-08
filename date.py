import pandas as pd
import datetime as dt
import numpy as np

file='temp.csv'
temp=pd.read_csv(file)

temp['avgs']=np.nan
temp['avga']=np.nan
temp['phase']=np.nan

n=len(temp)
for i in range(n):
	date=dt.datetime.strptime(temp.loc[i]['date'],"%m/%d/%y %H:%M").strftime("%m/%d/%y %H:%M")
	sensor=temp['sensor'][i]
	ambient=temp['ambient'][i]
	if i==0:
		avgs=temp.loc[i]['sensor']
		avga=temp.loc[i]['ambient']
	else:
		avgs=(temp.loc[i]['sensor']+temp.loc[i-1]['sensor'])/2
		avga=(temp.loc[i]['ambient']+temp.loc[i-1]['ambient'])/2
	if sensor>=10 and sensor<=45:
		phase='Mesophillic'
	elif sensor>45 and sensor<=70:
		phase='Thermophillic'
	else:
		phase='Out of Range'
	temp.loc[i]=[date,sensor,ambient,avgs,avga,phase]

temp.to_csv('tempPy.csv',sep=',',index=False)
