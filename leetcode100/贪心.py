#encoding:utf-8
'''
1.分配问题 分饼干与分糖果问题
2.区间问题
'''
'''
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
'''
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i,j=0,0
        while i<len(s) and j<len(g):
            if s[i]>=g[i]:
                i+=1
                j+=1
            else:
                j+=1
        return i



# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #按照区间结尾进行赠序排列，区间结尾越小，预留的越大
        if not intervals:
            return 0
        intervals.sort(key=lambda value:value[1])
        cur_location = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < cur_location:
                res += 1
            else:
                cur_location = intervals[i][1]
        return res


#练习
# 605，452，763，122，406，665
# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
'''
题解：如果当前及左右三个位置中存在1，则跳过，否则可以种花，种完花n减1,即flowerbed[i]=1,n-=1
当n==0时，说明已经种完花了，返回True
如果最后不满足上述条件，则返回False
'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # count, m, prev = 0, len(flowerbed), -1
        # for i in range(m):
        #     if flowerbed[i] == 1:
        #         if prev < 0:
        #             count += i // 2
        #         else:
        #             count += (i - prev - 2) // 2
        #         prev = i
        # if prev < 0:
        #     count += (m + 1) // 2
        # else:
        #     count += (m - prev - 1) // 2
        #
        # return count >= n
        if n == 0:
            return True
        m = len(flowerbed)
        for i in range(m):
            # 判断当前及左右位置是否种植了花
            if flowerbed[i] == 1:
                continue
            if i > 0 and flowerbed[i - 1] == 1:
                continue
            if i + 1 < m and flowerbed[i + 1] == 1:
                continue
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True
        return False


#452最小数量射爆气球
#转换为数学问题
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        if len(points)<=1:
            return len(points)
        nums=0
        for i in range(len(points)-1):
            if points[i][1]>=points[i+1][0] and points[i][1]<=points[i+1][1]:
                nums+=1
                i+=1
        return nums
    def leetcode_findMinArrowShots(self,points):
        if not points:
            return 0

        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1

        return ans

#763字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
'''
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
'''
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        #显然同一个字母的第一次出现的下标位置和最后一次出现的下标位置必须出现在同一个片段。
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition

        last=[0]*26
        for i ,ch in enumerate(s):
            last[orf(ch)-ord('a')]=i
        start,end=0,0
        patition=list()
        for i,ch in enumerate(s):
            end=max(end,last[ord(ch)-ord('a')])
            if i==end:
                partition.append(end-start+1)
                start=end+1
        return patition

#122给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

'''
[7,1,5,3,6,4]
转换为数学问题 不相交的[l,r]区间是的sum(price[r]-price[l])最大
又已知 price[ri]-price[li]=price[ri]-price[ri-1]+price[ri-1]+price[ri-2}+......
找到区间x个区间为1 的(l1,li+1)是的最大
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans=0
        for i in range(1,len(prices)):
            ans+=max(0,prices[i]-prices[i-1])
        return ans

#406假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。
# 每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
# 请你重新构造并返回输入数组 people 所表示的队列。
# 返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。



# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
'''
[4,2,3]
'''
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if i + 2 < n and nums[i] > nums[i + 2]:  # 特殊情况
                    nums[i] = nums[i + 1]
                else:  # 常规情况
                    i+2>=n
                    nums[i + 1] = nums[i]
                break
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True


if __name__ == '__main__':
    a=Solution()
    print(a.leetcode_findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))