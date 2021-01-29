#encoding:utf-8

import numpy as np
import time
def dataload(filename):
    '''
        加载文件
        :param fileName:要加载的文件路径
        :return: 数据集和标签集
    '''
    dataarr=[]
    lablearr=[]
    fr=open(filename)
    for line in fr.readline():
        # 获取当前行，并按“，”切割成字段放入列表中
        # strip：去掉每行字符串首尾指定的字符（默认空格或换行符）
        # split：按照指定的字符将字符串切割成每个字段，返回列表形式
        curLine = line.strip().split(',')
        # 将每行中除标记外的数据放入数据集中（curLine[0]为标记信息）
        # 在放入的同时将原先字符串形式的数据转换为整型
        dataarr.append([int(num) for num in curLine[1:]])
        lablearr.append((int(curLine[0])))
    return dataarr,lablearr


def calcdict(x1,x2):
    '''
    计算两个样本点向量之间的距离
    使用的是欧氏距离，即 样本点每个元素相减的平方  再求和  再开方
    欧式举例公式这里不方便写，可以百度或谷歌欧式距离（也称欧几里得距离）
    :param x1:向量1
    :param x2:向量2
    :return:向量之间的欧式距离
    '''

    return np.sqrt(np.sum(np.square(x1-x2)))

    #曼哈顿距离
    #return np.sum(x1-x2)

def getClosest(trainDataMat, trainLabelMat, x, topK):
    '''
    预测样本x的标记。
    获取方式通过找到与样本x最近的topK个点，并查看它们的标签。
    查找里面占某类标签最多的那类标签
    （书中3.1 3.2节）
    :param trainDataMat:训练集数据集
    :param trainLabelMat:训练集标签集
    :param x:要预测的样本x
    :param topK:选择参考最邻近样本的数目（样本数目的选择关系到正确率，详看3.2.3 K值的选择）
    :return:预测的标记
    '''

    datalist=[0]*len(trainDataMat)
    for i in range(len(trainDataMat)):
        x1=trainDataMat[i]
        curdist=calcdict(x1,x)
        datalist[i]=curdist

    #排序
    topKList = np.argsort(np.array(datalist))[:topK]
    lablelist=[0]*10
    for index in topKList:
        # trainLabelMat[index]：在训练集标签中寻找topK元素索引对应的标记
        # int(trainLabelMat[index])：将标记转换为int（实际上已经是int了，但是不int的话，报错）
        # labelList[int(trainLabelMat[index])]：找到标记在labelList中对应的位置
        # 最后加1，表示投了一票
        lablelist[int(trainLabelMat[index])] += 1
    return lablelist.index(max(lablelist))


def test(trainDataArr, trainLabelArr, testDataArr, testLabelArr, topK):
    '''
    测试正确率
    :param trainDataArr:训练集数据集
    :param trainLabelArr: 训练集标记
    :param testDataArr: 测试集数据集
    :param testLabelArr: 测试集标记
    :param topK: 选择多少个邻近点参考
    :return: 正确率
    '''

    print('start test')
    #将所有列表转换为矩阵形式，方便运算
    trainDataMat = np.mat(trainDataArr); trainLabelMat = np.mat(trainLabelArr).T
    testDataMat = np.mat(testDataArr); testLabelMat = np.mat(testLabelArr).T

    errorCnt=0
    for i in range(200):
        # print('test %d:%d'%(i, len(trainDataArr)))
        print('test %d:%d' % (i, 200))
        # 读取测试集当前测试样本的向量
        x = testDataMat[i]
        # 获取预测的标记
        y = getClosest(trainDataMat, trainLabelMat, x, topK)
        # 如果预测标记与实际标记不符，错误值计数加1
        if y != testLabelMat[i]: errorCnt += 1
        # 返回正确率
        # return 1 - (errorCnt / len(testDataMat))
    return 1 - (errorCnt / 200)

if __name__ == "__main__":
    start = time.time()
    #获取训练集
    trainDataArr, trainLabelArr = dataload('../Mnist/mnist_train.csv')
    #获取测试集
    testDataArr, testLabelArr = dataload('../Mnist/mnist_test.csv')
    #计算测试集正确率
    accur = test(trainDataArr, trainLabelArr, testDataArr, testLabelArr, 25)
    #打印正确率
    print('accur is:%d'%(accur * 100), '%')
    end = time.time()
    #显示花费时间
print('time span:', end - start)