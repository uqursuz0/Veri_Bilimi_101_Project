from dataclasses import dataclass
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def dataPreView(sample):
    print(sample.describe()+'\n'+sample.info()+'\n'+sample.head())

dataset=pd.read_csv("Highest Holywood Grossing Movies.csv")
#print(dataset.columns)
dataset=dataset.drop(["Movie Info","Unnamed: 0","Distributor","License"],axis=1)
print(dataset.head())
dataset.to_csv("dataset_1.0.1.csv",index=None)