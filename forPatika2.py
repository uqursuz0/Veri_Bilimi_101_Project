import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv("dataset_1.0.1.csv")
temp_yearlist=[]
temp_titlelist=[]
for i in (dataset["Title"]):
    yearlist=str(i).split()
    newyearlist=yearlist[-1]
    temp_yearlist.append(newyearlist[1:-1])
    temp_titlelist.append(" ".join(yearlist[0:-1]))
for a in range(len(dataset["Title"])):
    dataset["Release Date"].update(temp_yearlist)
    dataset["Title"].update(temp_titlelist)
dataset.to_csv("dataset_1.1.0.csv",index=None)
dataset.to_excel("dataset.xlsx",index=None)
    
