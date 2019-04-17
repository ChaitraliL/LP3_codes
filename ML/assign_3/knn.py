import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from itertools import islice

def plot(pos_x,pos_y,neg_x,neg_y):
    plt.scatter(pos_x,pos_y,c="red")
    plt.scatter(neg_x,neg_y,c="blue")
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("knn")
    plt.grid("True")
    plt.show()

def create_dataset():
    d = {'x':[2,4,4,6,4,6], 'y':[4,6,2,4,4,2], 'class':[1,1,1,1,0,0]}
    df = pd.DataFrame(data=d, columns=['x','y','class'])
    pos_x = []
    pos_y = []
    neg_x = []
    neg_y = []
    for index,row in df.iterrows():
        if row['class'] == 1:
            pos_x.append(row['x'])
            pos_y.append(row['y'])
        else:
            neg_x.append(row['x'])
            neg_y.append(row['y'])

    plot(pos_x,pos_y,neg_x,neg_y)

    return df

def find_class(df,x,y,k):
    dic = {}
    for index,row in df.iterrows():
        dist =  math.sqrt((row['x'] - x)**2 + (row['y'] - y)**2)
        dic[index] = dist
    sorted_dis = sorted(dic.items(), key=lambda kv: kv[1])
    pos = []
    pos.append(sorted_dis[0][0])
    pos.append(sorted_dis[1][0])
    pos.append(sorted_dis[2][0])
    labels = []
    for index,row in df.iterrows():
        if index in pos:
            labels.append(row['class'])
    pos = 0
    neg = 0
    for v in labels:
        if v == 1:
            pos += 1
        else:
            neg += 1
    if (pos > neg):
        print("positive")
    else:
        print("negative")

def main():
    df = create_dataset()
    find_class(df,6,6,3)

if __name__ == "__main__":
    main()
