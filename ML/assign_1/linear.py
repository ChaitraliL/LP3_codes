import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

def covariance(X,mean_x,Y,mean_y): #np.cov(X,Y)[0][1] can be used as well
    cov = 0.0
    for i in range(len(X)):
        cov += (X[i] - mean_x) * (Y[i] - mean_y)
    return cov

def variance(values,mean): #np.var(values) can also be used
    var = sum([(x - mean)**2 for x in values])
    return var

def findcoefficients(X,Y):
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    b0 = covariance(X,mean_x,Y,mean_y) / variance(X,mean_x)
    b1 = mean_y - b0 * mean_x
    return [b0,b1]

def predict(cf,X):
    predicted = [(cf[0]*value+cf[1]) for value in X]
    return predicted

def plot(X,Y,predicted):
    plt.scatter(X, Y, color = "m", marker = "o", s = 30)
    plt.plot(X,predicted,color = "g")
    plt.show()

def r_value(X,Y):
    xy = [(x*y) for (x,y) in zip(X,Y)]
    x_sq = [(x**2) for x in X]
    y_sq = [(y**2) for y in Y]

    x_sum, y_sum, xy_sum, x_sq_sum, y_sq_sum = sum(X), sum(Y), sum(xy), sum(x_sq), sum(y_sq)
    r = (len(X) * xy_sum - x_sum * y_sum) / (sqrt( (len(X)*x_sq_sum - x_sum**2) * (len(Y)*y_sq_sum - y_sum**2) ))
    return r

def main():
    X = np.array([10,9,2,15,10,16,11,16])
    Y = np.array([95,80,10,50,45,98,38,93])
    r = r_value(X,Y)
    print("Correlation measure is %8.2f" % r)
    print("r-square value is %8.2f" % (r * r * 100))
    cf = findcoefficients(X,Y)
    print("parameters: %8.2f , %8.2f" % (cf[0],cf[1]))
    predicted = predict(cf,X)
    plot(X,Y,predicted)

if __name__ == "__main__":
    main()
