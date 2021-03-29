#encoding:utf-8
'''
Sorted Array
     Merge Two Sorted Arrays / Merge k Sorted Arrays
     Median Of Two Sorted Arrays
Subarray
    Best Time to Buy and Sell Stocks I, II, III
    Subarray I, II, III, IV
Two Pointers
    Two sum, 3Sum, 4Sum, k Sum, 3Sum Closest
    Partition Array
'''
#merge sorter array
class Solution:
    '''
    双指针法
    '''
    def intersect(self, nums1, nums2):
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        result = []
        nums1.sort()
        nums2.sort()
        left = 0
        right = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] > nums2[right]:
                right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                result.append(nums1[left])
                left += 1
                right += 1
        return result



# 14z最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]





