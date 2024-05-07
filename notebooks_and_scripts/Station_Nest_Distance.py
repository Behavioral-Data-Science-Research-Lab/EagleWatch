# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:16:14 2024

@author: lfwei
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import haversine as hs
#%%
concat_data=pd.read_csv('Concatenated Data.csv')
station_loc=pd.read_csv('Station Lat.Long.csv')
#%%
closest_station=[]
distance=[]

for i in range(len(concat_data)):
    nest_lat=concat_data['Latitude'][i]
    nest_long=concat_data['Longitude'][i]
    short_dist=100_000
    short_stat='none'
    for j in range(len(station_loc)):
        stat_lat=station_loc['LATITUDE'][j]
        stat_long=station_loc['LONGITUDE'][j]
        
        dist=hs.haversine((nest_lat,nest_long),(stat_lat,stat_long))
        if dist < short_dist:
            short_stat=station_loc['STATION'][j]
            short_dist=dist
        else:
            continue
    closest_station.append(short_stat)
    distance.append(short_dist)
        
concat_data['Station']=closest_station
concat_data['Distance']=distance   
#%%
concat_data['Occupied'].unique()  
#%%
concat_data['Active'].unique()
#%%
concat_data['Successful'].unique()
#%%
concat_data['Occupied']=concat_data['Occupied'].replace({'Yes':1,'yes':1,'y':1,'Y':1,
                                                         'No':0,'no':0,'N':0,
                                                         'Unknown':-1,'Unk':-1,'UNK':-1,'unk':-1})
concat_data['Active']=concat_data['Active'].replace({'Yes':1,'y':1,'Y':1,
                                                         'No':0,'no':0,'N':0,'n':0,
                                                         'Unknown':-1,'Unk':-1,'UNK':-1,'unk':-1})
concat_data['Successful']=concat_data['Successful'].replace({'Yes':1,'y':1,'Y':1,
                                                         'No':0,'no':0,'N':0,'N ':0,
                                                         'Unknown':-1,'Unk':-1,'UNK':-1,'unk':-1})
#concat_data['Occupied']=concat_data['Occupied'].replace('unk',np.nan)
#%% 
concat_data.to_csv('Concatenated Data_Location.csv',index=False)    