#encoding:utf-8
import numpy as np
import  time


def loaddata(filename):
    '''
    :param filename:
    :return: list 形式特征与目标值
    '''
    dataarr=[]
    lablearr=[]
    fr=open(filename,'r')
    for line in fr.readline():
        # 对每一行数据按切割福','进行切割，返回字段列表
        curline=line.strip().split(',')
        # Mnsit有0-9是个标记，由于是二分类任务，所以将>=5的作为1，<5为-1
        if int(curline[0])>=5:
            lablearr.append(1)
        else:
            lablearr.append(-1)
        dataarr.append(([int(num)/255 for num in curline[1:]]))
    # 返回data和label
    return dataarr,lablearr


def perceptron(dataarr,lablearr,iter=50):
    '''
    感知器训练过程
    :param dataArr:训练集的数据 (list)
    :param labelArr: 训练集的标签(list)
    :param iter: 迭代次数，默认50
    :return: 训练好的w和b
    '''
    print('start to trans')
    # 将数据转换成矩阵形式（在机器学习中因为通常都是向量的运算，转换称矩阵形式方便运算）
    # 转换后的数据中每一个样本的向量都是横向的
    datamat=np.mat(dataarr)
    # 将标签转换成矩阵，之后转置(.T为转置)。
    # 转置是因为在运算中需要单独取label中的某一个元素，如果是1xN的矩阵的话，无法用label[i]的方式读取
    # 对于只有1xN的label可以不转换成矩阵，直接label[i]即可，这里转换是为了格式上的统一
    labelMat = np.mat(lablearr).T
    m,n=np.shape(datamat)
    # 创建初始权重w，初始值全为0。
    # np.shape(dataMat)的返回值为m，n -> np.shape(dataMat)[1])的值即为n，与
    # 样本长度保持一致
    #初始化w
    w=np.zeros(1,np.shape(datamat)[1])
    # 初始化b
    b=0
    # 初始化步长，也就是梯度下降过程中的n，控制梯度下降速率
    h = 0.0001
    #批处理梯度下降
    for i in range(iter):
        #随机梯度下降
        for i in range(m):
            xi=datamat[i]
            yi=lablearr[i]
            #判断是否是误分类样本
            #误分类样本特诊为： -yi(w*xi+b)>=0，详细可参考书中2.2.2小节
            #在书的公式中写的是>0，实际上如果=0，说明改点在超平面上，也是不正确的
            if -1*yi*(w*xi.T+b)>=0:
                # 对于误分类样本，进行梯度下降，更新w和b
                w = w + h * yi * xi
                b = b + h * yi
                # 打印训练进度
        print('Round %d:%d training' % (i, iter))
            # 返回训练完的w、b
    return w, b


def test(dataarr,labelarr,w,b):
    '''
        测试准确率
        :param dataArr:测试集
        :param labelArr: 测试集标签
        :param w: 训练获得的权重w
        :param b: 训练获得的偏置b
        :return: 正确率
        '''
    # 将数据集转换为矩阵形式方便运算
    dataMat = np.mat(dataarr)
    # 将label转换为矩阵并转置，详细信息参考上文perceptron中
    # 对于这部分的解说
    labelMat = np.mat(labelarr).T
    # 获取测试数据集矩阵的大小
    m, n = np.shape(dataMat)
    # 错误样本数计数
    errorCnt = 0
    # 遍历所有测试样本
    for i in range(m):
        # 获得单个样本向量
        xi = dataMat[i]
        # 获得该样本标记
        yi = labelMat[i]
        # 获得运算结果
        result = -1 * yi * (w * xi.T + b)
        # 如果-yi(w*xi+b)>=0，说明该样本被误分类，错误样本数加一
        if result >= 0: errorCnt += 1
    # 正确率 = 1 - （样本分类错误数 / 样本总数）
    accruRate = 1 - (errorCnt / m)
    # 返回正确率
    return accruRate
if __name__ == '__main__':
    #获取当前时间
    #在文末同样获取当前时间，两时间差即为程序运行时间
    start = time.time()
    #获取训练集及标签
    trainData, trainLabel = loaddata('../Mnist/mnist_train.csv')
    #获取测试集及标签
    testData, testLabel = loaddata('../Mnist/mnist_test.csv')
    #训练获得权重
    w, b = perceptron(trainData, trainLabel, iter = 30)
    #进行测试，获得正确率
    accruRate = test(testData, testLabel, w, b)
    #获取当前时间，作为结束时间
    end = time.time()
    #显示正确率
    print('accuracy rate is:', accruRate)
    #显示用时时长
    print('time span:', end - start)







