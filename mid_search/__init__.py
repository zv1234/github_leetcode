#while 循环和递归写二分查找

# 二分法模版
def mind(nums,target):
    star=0
    end=len(nums)-1
    while star+1<end:
        #防止溢出
        mid=star+(end-star)/2
        if nums[mid]==target:
            end=mid
        elif nums[mid]<target:
            star=mid
        else:
            end=mid
    if nums[star]==target:
        return star
    if nums[end]==target:
        return end
    return -1



#69求开方 给定一个非负整数，求它的开方，向下取整。
'''
1.二分查找
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        l,r,ans=0,x,-1
        while l<=r:
            mid=l+(r-l)/2
            if mid*mid<=x:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans

#34给定一个增序的整数数组和一个值，查找该值第一次和最后一次出现的位置。
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==[]:
            return [-1,-1]
        l=0
        r=len(nums)-1
        while l<r:
            pass




