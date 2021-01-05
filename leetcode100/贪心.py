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
