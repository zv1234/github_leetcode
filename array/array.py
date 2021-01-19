#encoding:utf-8
'''
数组
'''

# 移动0 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。



#删除数组中重复项
'''
题解：双指针向前读取数组，i=0 j=1 如果相等则j向前加1，不相等都时候i位置向前加一后，nums[i]=nums[j]
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for j in range(1,len(nums)):
            if nums[i]==nums[j]:
                j+=1
            else:
                i+=1
                nums[i]=nums[j]
        return i+1


#买卖股票都最佳时机


#存在重复元素
# 给定一个整数数组，判断是否存在重复元素。
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #取了个巧
        return len(nums) != len(set(nums))



# 给出一个区间的集合，请合并所有重叠的区间。
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # n=len(intervals)
        # a=0
        # intervals.sort(key=lambda value:value[0])
        # for i in range(len(intervals)-1):
        #     if intervals[i+1][0]<=intervals[i][1]<=intervals[i+1][1]:
        #         intervals[i+1][0]=intervals[i][0]
        #         a+=1
        # return intervals[a:]
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged