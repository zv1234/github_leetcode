#encoding:utf-8

# 242有效的字母异位词
class Solution:
    def isAnagram(self, s, t) :
        list1=[0]*26
        for i in range(len(s)):
            index=ord(s[i])-ord('a')
            list1[index]+=1
        for i in range(len(t)):
            index_t=ord(t[i])-ord('a')
            list1[index_t]-=1
        for i in list1:
            if i==0:
                continue
            else:
                return False
        return True

#349两个数组的交集
class Solution:
    def intersection(self, nums1, nums2):
        nums1=set(nums1)
        nums2=set(nums2)
        reslut=[]
        for i in nums1:
            if i in nums2:
                reslut.append(i)
        return reslut

# 202快乐数
class Solution:
    def isHappy(self, n) :

        def get_sum(m):
            get_sum = 0
            for i in range(len(str(m))):
                get_sum += (int(str(m)[i]) * int(str(m)[i]))
            return get_sum

        list1 = [n]
        while 1:
            next_sum = get_sum(n)
            if next_sum == 1:
                return True
            else:
                if next_sum in list1:
                    return False
                list1.append(next_sum)
                n = next_sum

# 454四数相加
class Solution:
    def fourSumCount(self, A, B, C, D):
        dict1 = {}
        count = 0
        for i in A:
            for j in B:
                if i + j not in dict1:
                    dict1[i + j] = 1
                else:
                    dict1[i + j] += 1
        for m in C:
            for n in D:
                if 0 - m - n in dict1:
                    count += dict1[0 - m - n]
        return count


#383赎金信
class Solution:
    def canConstruct(self, ransomNote, magazine):
        list1 = [0] * 26
        list2 = [0] * 26
        if not ransomNote:
            return True
        for i in range(len(magazine)):
            index = ord(magazine[i]) - ord('a')
            list1[index] += 1
        for j in range(len(ransomNote)):
            index = ord(ransomNote[j]) - ord('a')
            list1[index] -= 1
            if list1[index] < 0:
                return False
        return True


#15三数之和
class Solution:
    def threeSum(self, nums):
        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        nums.sort()
        res=[]
        for i in range(n):
            if(nums[i]>0):
                return res
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return res



#18四数之和
class Solution:
    def fourSum(self, nums, target):
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets

        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets






