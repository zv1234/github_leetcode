# 快排
def kp(arr, i, j):
    if i < j:
        base = kpgc(arr, i, j)
        kp(arr, i, base)
        kp(arr, base + 1, j)


def kpgc(arr, i, j):
    base = arr[i]
    while i < j:
        while i < j and arr[j] >= base:
            j -= 1
        while i < j and arr[j] < base:
            arr[i] = arr[j]
            i += 1
            arr[j] = arr[i]
    arr[i] = base
    return i


# 归并排序 分治算法
class sort(object):
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2  # 得到整数的中位数
        # 分别对左右两部分进行排序
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        # 将排好序的数组进行合并
        return self.merge(left, right)

    def merge(self, left, right):
        # i,j分别代表左右部分的起始位置，res暂存排完序的数组
        i, j, res = 0, 0, []
        # 当左半部分和右半部分，有一个搜索完毕，则结束while循环
        while i < len(left) and j < len(right):
            # 如果左半部分的值小于右半部分的值，则将左半部分的值添加到res中
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            # 否则，将右半部分的值，添加到res中。
            else:
                res.append(right[j])
                j += 1
        # 将左半部分或右半部分的剩余值添加到res中。
        res += left[i:] or right[j:]
        return res


# 插入排序
def insert(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        a = i
        while key < nums[a - 1]:
            nums[a] = nums[a - 1]
            a = a - 1
            if a - 1 < 0:
                break
        nums[a] = key
    return nums


# 冒泡排序


# 在一个未排序的数组中，找到第k大的数字。在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
'''
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
'''


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def kp(arr, i, j):
            base = arr[i]
            while i < j:
                while i < j and arr[j] >= base:
                    j -= 1
                while i < j and arr[j] < base:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i] = base
            return i
        l=0
        r=len(nums)-1
        while 1:
            base = kp(nums, l, r)
            if base==k:
                return nums[base]
            if base<k:
                l=base+1
            if base>k:
                r=base
        return


    def right_leetcode(self,nums,k):

        def partition(self,left, right,nums):
            pivot = nums[left]
            l = left + 1
            r = right
            while l <= r:
                if nums[l] < pivot and nums[r] > pivot:
                    nums[l], nums[r] = nums[r], nums[l]
                if nums[l] >= pivot:
                    l += 1
                if nums[r] <= pivot:
                    r -= 1
            nums[r], nums[left] = nums[left], nums[r]
            return r

        left = 0
        right = len(nums) - 1
        while 1:
            idx = partition(left, right)
            if idx == k - 1:
                return nums[idx]
            if idx < k - 1:
                left = idx + 1
            if idx > k - 1:
                right = idx - 1
        return


#桶排序
def bucketSort(nums):
    # 选择一个最大的数
    max_num = max(nums)
    # 创建一个元素全是0的列表, 当做桶
    bucket = [0] * (max_num + 1)
    # 把所有元素放入桶中, 即把对应元素个数加一
    for i in nums:
        bucket[i] += 1

    # 存储排序好的元素
    sort_nums = []
    # 取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_nums.append(j)

    return sort_nums
nums=[1,1,2,1,2,3]
print(bucketSort(nums))


#给定一个数组，求前k个最频繁的数字。
'''
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 选择一个最大的数
        dict1={}
        for i in nums:
            if i in dict1:
                dict1[i]=0
            else:
                dict1[i]+=1
        sort_num = []
        sort(dict1.items(),key=lambda x:x[1],reverse=True)
        for i in range(len(dict1[:k])):
            sort_num.append(dict1[i][0])
        return sort_num




#75很经典的荷兰国旗问题，考察如何对三个重复且打乱的值进行排序。