import numpy as np
import random
import math


def derivative(X):
    for i in range(len(X)):
        for j in range(len(X[0])):
            X[i][j] = -((X[i][j]/2)/((X[i][j]+1))**2)
    return X


def giperTang(W, m):
    for i in range(len(W)):
        for j in range(m):
            for k in range(m - 1):
                W[i][j] = math.tanh(W[i][j] - k)
    return W


def progn(W1, contDat, W3, T_2, W2, T_3, len_progn):
    for i in range(len_progn):
        per = np.array([50, 100, 200])
        pre_rez = Hid(fullOper(per, W1), fullOper(contDat, W3), T_2)
        result = siggmThan(fullOper(siggmThan(pre_rez), W2) - T_3)
        print(round(result[0]))


################################

def creRand(cols, row):
    for j in range(cols):
        a = random.random() * 2 - 1
        row.append(a)
    return row

def randomWeight(rows, cols):
    res = []
    for i in range(rows):
        row = []
        row = creRand(cols, row)
        res.append(row)
    arr = np.array(res)
    return arr


def sigThan(len_rang,matrix,res):
    for i in range(len_rang):
        if matrix[i] < 0: res = np.append(res, matrix[i] * 0.1)
        else: res = np.append(res, matrix[i])
    return res

def siggmThan(matrix):
    res = np.array([])
    len_rang = len(matrix)
    res = sigThan(len_rang,matrix,res)
    return res


def fullOper(a, b):
    return a @ b