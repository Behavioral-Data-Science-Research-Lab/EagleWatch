# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:20:40 2024

@author: lfwei
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import haversine as hs
import pgeocode as pgeo
#%%
concat_data=pd.read_csv("concat_data_loc_year.csv")
pop_data=pd.concat(pd.read_excel('Flcopops_Edit.xlsx',sheet_name=None),ignore_index=False)
#%%
pop_year=pd.merge(concat_data,pop_data)
pop_year=pop_year.drop(['Unincorporated', '% of Total','Incorporated','% of Total.1'],axis=1)