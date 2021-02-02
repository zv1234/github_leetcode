#encoding:utf-8

#二分查找问题描述
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if not nums or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            # 细节，不写成(start + end) / 2：为了防止溢出2^32
            mid = int((end - start) / 2 + start)
            # mid = ((end - start) >> 1) + start #注意python运算符和优先级
            if target == nums[mid]:
                end = mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

#第一个错误的代码版本
'''
代码库的版本号是从 1 到 n 的整数。某一天，有人提交了错误版本的代码，因此造成自身及之后版本的代码在单元测试中均出错。请找出第一个错误的版本号。
'''
#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if n < 1:
            return -1
        if n == 1 and SVNRepo.isBadVersion(1):
            return 1
        start = 1
        end = n
        while start + 1 < end:
            mid = int((end - start) / 2 + start)
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
        if SVNRepo.isBadVersion(start):
            return start
        if SVNRepo.isBadVersion(end):
            return end
        return -1


#在大数组中查找
'''
给一个按照升序排序的正整数数组。这个数组很大以至于你只能通过固定的接口 ArrayReader.get(k) 来访问第k个数。(或者C++里是ArrayReader->get(k))，
并且你也没有办法得知这个数组有多大。找到给出的整数target第一次出现的位置。你的算法需要在O(logk)的时间复杂度内完成，k为target第一次出现的位置的下标。
如果找不到target，返回-1。
'''
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if not reader:
            return -1
        start = 0
        end = 1
        while reader.get(end) < target:
            end *= 2
        while start + 1 < end:
            mid = int((end - start) / 2 + start)
            if reader.get(mid) == target:
                end = mid
            elif reader.get(mid) > target:
                end = mid
            else:
                start = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1

#寻找排序旋转数组中最小值
'''
159假设一个排好序的数组在其某一未知点发生了旋转（比如0 1 2 4 5 6 7 可能变成4 5 6 7 0 1 2）。你需要找到其中最小的元素。
'''
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        star=0
        end=len(nums)-1
        while star+1<end:
            mid=(end-star)//2+star
            if nums[mid]<nums[end]:
                end=mid
            else:
                star=mid
        if nums[star]<nums[end]:
            return nums[star]
        return nums[end]

#28搜索二维矩阵
'''
描述
ENG
写出一个高效的算法来搜索 m × n矩阵中的值。
这个矩阵具有以下特性：
每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。
'''