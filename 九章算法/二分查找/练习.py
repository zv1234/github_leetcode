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


#61搜索区间
'''
给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。
如果目标值不在数组中，则返回[-1, -1]
'''


class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        # write your code here
        if not A or len(A) == 0:
            return [-1, -1]

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = int((end - start) / 2 + start)
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            leftBound = start
        elif A[end] == target:
            leftBound = end
        else:
            return [-1, -1]
        start, end = leftBound, len(A) - 1
        while start + 1 < end:
            mid = int((end - start) / 2 + start)
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            rightBound = end
        else:
            rightBound = start
        return [leftBound, rightBound]

#585. 山脉序列中的最大值
'''
给 n 个整数的山脉数组，即先增后减的序列，找到山顶（最大值)
'''
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if len(nums)==0:
            return -1
        start=0
        end=len(nums)-1
        while start+1<end:
            mid=int((end-start)/2)+start
            if nums[mid]>nums[mid+1]:
                end=mid
            else:
                start=mid
        if nums[start]>nums[end]:
            return nums[start]
        else:
            return  nums[end]

# 75. 寻找峰值
'''
你给出一个整数数组(size为n)，其具有以下特点：
相邻位置的数字是不同的
A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。
'''
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if len(A)==1:
            return A[0]
        start=0
        end=len(A)-1
        while start+1<end:
            mid=((end-start)>>1)+start
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                return mid
            elif A[mid-1]<A[mid]<A[mid+1]:
                start=mid
            else:
                end=mid
        return -1

# 141 x的开方
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        if x <= 1:
            return x
        start = 1
        end = x
        while start + 1 < end:
            mid = start + (end - start) >> 1
            if mid * mid <= x and (mid + 1) * (mid + 1) >= x:
                return mid
            if mid * mid > x:
                end = mid
            else:
                start = mid
        return 0
