#encoding:utf-8
'''
贪心算法了解

本质：选择每一阶段局部最优，从而全局最优

解题步骤
1。将问题分解为若干个子问题
2。找到适合的贪心策略
3。求解每个子问题的最优解
4。将局部最优解堆叠成全局最优解

'''

# 455分发饼干
'''
局部最优大饼干优先最大的胃口
或者小饼干优先最小的胃口
'''
class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i,j=0,0
        while i<len(g) and j <len(s):
            if g[i]<=s[j]:
                i+=1
            j+=1
        return i

#376摆动序列
class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums)<=1:
            return len(nums)
        cur_dif=0
        pre_dif=0
        result=1
        for i in range(len(nums)-1):
            cur_dif=nums[i+1]-nums[i]
            if (cur_dif>0 and pre_dif<=0) or (cur_dif<0 and pre_dif>=0):
                result+=1
                pre_dif=cur_dif
        return result

#122买卖股票的最佳时机
#贪心与动态规划
class Solution:
    def maxProfit(self, prices):
        result=0
        for i in range(len(prices)-1):
            result+=max(prices[i+1]-prices[i],0)
        return result


#55跳跃游戏I
#没做出来
class Solution:
    def canJump(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i


# 45跳跃游戏II


#1005 k次取反后最大化的数组和



#134加油站

