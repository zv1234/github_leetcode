#encoding:utf-8
#78给定⼀组不含重复元素的整数数组 nums，返回该数组所有可能的⼦集（幂集）。
# 说明：解集不能包含重复的⼦集。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path=[]
        result=[]
        #递归参数
        def backstrack(nums,index):
            result.append(path[:])
            #递归出口
            if index>len(nums):
                return
            #递归单层逻辑
            for i in range(index,len(nums)):
                path.append(nums[i])
                backstrack(nums,i+1)
                path.pop()
        backstrack(nums,0)
        return result

#491 给定⼀个整型数组, 你的任务是找到所有该数组的递增⼦序列，递增⼦序列的⻓度⾄少是2。
# 示例:
# 输⼊: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# 说明:
# 给定数组的⻓度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的⼀种情况。