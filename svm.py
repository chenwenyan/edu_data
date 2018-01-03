# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt
import time
import random
import re

def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    with open(fileName) as fr:
        for line in fr.readlines():
            regex = re.compile('\s+')
            lineArr = regex.split(line.strip())
            dataMat.append([float(lineArr[0]), float(lineArr[1])])
            labelMat.append(float(lineArr[2]))
    return dataMat, labelMat

def selectJrand(i, m):
    j = i
    while (j == i):
        j = int(random.uniform(0, m))#从0到m随机采样，左闭右开
    return j

def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj

class optStruct:
    def __init__(self, dataMatIn, classLabels, C, toler):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = numpy.shape(dataMatIn)[0] #shape读取矩阵的长度
        self.alphas = numpy.mat(numpy.zeros((self.m, 1)))
        self.b = 0
        self.eCache = numpy.mat(numpy.zeros((self.m, 2)))

def calcEk(oS, k):
    fXk = float(numpy.multiply(oS.alphas, oS.labelMat).T * (oS.X * oS.X[k, :].T)) + oS.b
    Ek = fXk - float(oS.labelMat[k])
    return Ek

def selectJ(i, oS, Ei):
    maxK = -1
    maxDeltaE = 0
    Ej = 0
    oS.eCache[i] = [1, Ei]
    validEcacheList = numpy.nonzero(oS.eCache[:, 0].A)[0]
    if (len(validEcacheList)) > 1:
        for k in validEcacheList:
            if k == i:
                continue
            Ek = calcEk(oS, k)
            deltaE = abs(Ei - Ek)
            if (deltaE > maxDeltaE):
                maxK = k
                maxDeltaE = deltaE
                Ej = Ek
        return maxK, Ej
    else:
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS, j)
    return j, Ej

def updateEk(oS, k):
    Ek = calcEk(oS, k)
    oS.eCache[k] = [1, Ek]

def innerL(i, oS):
    Ei = calcEk(oS, i)
    if ((oS.labelMat[i] * Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or ((oS.labelMat[i] * Ei > oS.tol) and (oS.alphas[i] > 0)):
        j, Ej = selectJ(i, oS, Ei)
        alphaIold = oS.alphas[i].copy()
        alphaJold = oS.alphas[j].copy()
        if (oS.labelMat[i] != oS.labelMat[j]):
            L = max(0, oS.alphas[j] - oS.alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])
        if (L == H):
            # print("L == H")
            return 0
        eta = 2.0 * oS.X[i, :] * oS.X[j, :].T - oS.X[i, :] * oS.X[i, :].T - oS.X[j, :] * oS.X[j, :].T
        if eta >= 0:
            # print("eta >= 0")
            return 0
        oS.alphas[j] -= oS.labelMat[j] * (Ei - Ej) / eta
        oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
        updateEk(oS, j)
        if (abs(oS.alphas[j] - alphaJold) < 0.00001):
            # print("j not moving enough")
            return 0
        oS.alphas[i] += oS.labelMat[j] * oS.labelMat[i] * (alphaJold - oS.alphas[j])
        updateEk(oS, i)
        b1 = oS.b - Ei - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :] * oS.X[i, :].T - oS.labelMat[j] * (oS.alphas[j] - alphaJold) * oS.X[i, :] * oS.X[j, :].T
        b2 = oS.b - Ei - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :] * oS.X[j, :].T - oS.labelMat[j] * (oS.alphas[j] - alphaJold) * oS.X[j, :] * oS.X[j, :].T
        if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]):
            oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]):
            oS.b = b2
        else:
            oS.b = (b1 + b2) / 2.0
        return 1
    else:
        return 0

def smoP(dataMatIn, classLabels, C, toler, maxIter, kTup=('lin', 0)):
    """
    输入：数据集, 类别标签, 常数C, 容错率, 最大循环次数
    输出：目标b, 参数alphas
    """
    oS = optStruct(numpy.mat(dataMatIn),  numpy.mat(classLabels).transpose(), C, toler)
    iterr = 0
    entireSet = True
    alphaPairsChanged = 0
    while (iterr < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        if entireSet:
            for i in range(oS.m):
                alphaPairsChanged += innerL(i, oS)
            # print("fullSet, iter: %d i:%d, pairs changed %d" % (iterr, i, alphaPairsChanged))
            iterr += 1
        else:
            nonBoundIs = numpy.nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            for i in nonBoundIs:
                alphaPairsChanged += innerL(i, oS)
                # print("non-bound, iter: %d i:%d, pairs changed %d" % (iterr, i, alphaPairsChanged))
            iterr += 1
        if entireSet:
            entireSet = False
        elif (alphaPairsChanged == 0):
            entireSet = True
            # print("iteration number: %d" % iterr)
    return oS.b, oS.alphas

def calcWs(alphas, dataArr, classLabels):
    """
    输入：alphas, 数据集, 类别标签
    输出：目标w
    """
    X =numpy.mat(dataArr)
    labelMat =numpy.mat(classLabels).transpose()
    m, n =numpy.shape(X)
    w =numpy.zeros((n, 1))
    for i in range(m):
        w += numpy.multiply(alphas[i] * labelMat[i], X[i, :].T)
    return w

def plotFeature(dataMat, labelMat, weights, b):
    dataArr =  numpy.array(dataMat)
    n =  numpy.shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 0])
            ycord1.append(dataArr[i, 1])
        else:
            xcord2.append(dataArr[i, 0])
            ycord2.append(dataArr[i, 1])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x =numpy.arange(2, 7.0, 0.1)
    y = (-b[0, 0] * x) - 10 /numpy.linalg.norm(weights)
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()

def main():
    trainDataSet, trainLabel = loadDataSet('data/testcvm.txt')
    b, alphas = smoP(trainDataSet, trainLabel, 0.6, 0.0001, 40)
    ws = calcWs(alphas, trainDataSet, trainLabel)
    print("ws = \n", ws)
    print("b = \n", b)
    plotFeature(trainDataSet, trainLabel, ws, b)

if __name__ == '__main__':
    start = time.clock()
    main()
    end = time.clock()
    print('finish all in %s' % str(end - start))