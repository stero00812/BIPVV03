# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:03:53 2017

@author: Jonathan
"""
import datetime
import numpy as np
import pandas as pd
#############################Thermal

def Thermal(date_from,date_to):
#Ouvrir un dataframe thermique
    chemin='C:/Users/Jonathan/Desktop/20175_BIPV_V0.3.txt'
    Data=pd.read_csv(chemin,index_col=0,skip_blank_lines=True,skiprows=1,header=None)

    #Data.columns=['1L4','1L8','1M1','1M2','1M3','1M4','1M5','1M6','1M7','1M8','1R1','1R2','1R3','1R4','1R5','1R6','1R7','1R8','2M4','2M5','2M6','2M7','2M8','2R4','2R5','2R6','2R7','2R8','2L4','2L8','3M4','3M5','3M6','3M7','3M8','3R4','3R5','3R6','3R7','3R8','VL1','VL2','VR1','VR2','F1','F2','3L4','3L8']
    Data.columns=['3M6','3M7','3M8','3R4','3R5','3R6','3R7','3R8','VL1','VL2','VR1','VR2','F1','F2','3L4','3L8','1R7','1R8','2M4','2M5','2M6','2M7','2M8','2R4','2R5','2R6','2R7','2R8','2L4','2L8','3M4','3M5','1L4','1L8','1M1','1M2','1M3','1M4','1M5','1M6','1M7','1M8','1R1','1R2','1R3','1R4','1R5','1R6']

    Data.index= pd.to_datetime(Data.index)

    datefrom = datetime.datetime.strptime(date_from, '%Y/%m/%d %H:%M:%S')
    dateto = datetime.datetime.strptime(date_to, '%Y/%m/%d %H:%M:%S')       
    
    Data=(Data[datefrom:dateto])#On sélectionne les données entre les deux dates

    
    Temp2=Data[['1R4','1R5','1R6','1R7','1R8']]
    Temp2['Mean Cavity'] = Temp2.mean(axis=1)
    #print Temp2
    
    return Temp2
    
#############################Electrical
    
def Electrical(date_from,date_to):
#Ouvrir un fichier csv du Femtogrid, le stocker dans un dataframe & le retourner.

    chemin='C:/Users/Jonathan/Desktop/PO330LogFile8.csv'
    Data=pd.read_csv(chemin,sep=';', index_col=False)
    Data = Data[Data.TimeStamp != 'TimeStamp']
    Data['TimeStamp']= pd.to_datetime(Data['TimeStamp'],format='%m/%d/%Y %I:%M:%S %p')
    Data.index=Data.TimeStamp
    Data=Data.drop('TimeStamp',axis=1)

    Data=Data[['Pin[W]']]   
    
    return Data