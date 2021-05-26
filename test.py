# # 定义加密函数
# def jiami(x):
#     leng = len(bin(x).replace('0b', ''))
#     if leng == 8:
#         return int('0b' + (bin(x).replace('0b', '')[::-1]), 2)
#     else:
#         return int('0b' + ((8 - leng) * '0' + bin(x).replace('0b', ''))[::-1], 2)
#
#
# import cv2  # 需要下载python中opencv的库
# import numpy as np
#
# # 载入图片路径
# x = cv2.imread('/Users/zr/Downloads/系统架构图.jpg')
#
# # 调用函数加密
# i, j, k = x.shape  # 得到图片的三维数据（宽，长，3）
# y = np.zeros_like(x)
# for q in range(i):  # 调用两次循环逐点运算
#     for w in range(j):
#         for r in range(k):
#             y[q, w, r] = jiami(x[q, w, r])
#
# # 显示加密前图片（原图）
# cv2.namedWindow('x', 0)
# cv2.imshow('x', x)
# # 显示加密后图片
# cv2.namedWindow('y', 0)
# cv2.imshow('y', y)
# ########################################
# # 再次调用函数对加密后的图片运算，即解密
# i, j, k = y.shape
# z = np.zeros_like(y)
# for q in range(i):
#     for w in range(j):
#         for r in range(k):
#             z[q, w, r] = jiami(y[q, w, r])
#
# # 显示解密后图片
# cv2.namedWindow('z', 0)  # 处理因图片太大导致的窗口显示不够的问题
# cv2.imshow("z", z)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
with open("/Users/zr/Downloads/系统架构图.jpg",'rb') as f:
    conten=f.read()

