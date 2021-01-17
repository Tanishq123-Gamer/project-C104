import csv 
import pandas as pd 
import plotly.express as px

with open("SOCR-HeightWeight.csv",newline='') as f: 
    reader=csv.reader(f)
    data=list(reader)

print(data)

data.pop(0)
print(len(data))

new_data=[]

for a in range(len(data)):
    h= data[a][1]
    new_data.append(h)

print(new_data)

total=0

for x in new_data:
    total=total+float(x)

print(total/len(data))