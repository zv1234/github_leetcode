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
class Solution:
    def canCompleteCircuit(self, gas, cost):
        # count=0
        # reslut=0
        # start=0
        # for i in range(len(gas)):
        #     count+=(gas[i]-cost[i])
        #     reslut+=(gas[i]-cost[i])
        #     if count<0:
        #         start+=1
        #         count=0
        # if reslut<0:
        #     return -1
        # return start
        total, cur, ans = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:                     # 油不够开到i站
                cur = 0                     # cur置零，在新位置重新开始计算油耗情况
                ans = i + 1                 # 将起始位置改成i+1
        return ans if total >= 0 else -1


#135老师发糖果问题

#860柠檬水找零问题
class Solution:
    def lemonadeChange(self, bills):
# int five = 0, ten = 0, twenty = 0;
# for (int bill : bills) {
# // 情况⼀
# if (bill == 5) five++;
# // 情况⼆
# if (bill == 10) {
# if (five <= 0) return false;
# ten++;
# five--;
#  }
# // 情况三
# if (bill == 20) {
# // 优先消耗10美元，因为5美元的找零⽤处更⼤，能多留着就多留着
# if (five > 0 && ten > 0) {
# five--;
# ten--;
# twenty++; // 其实这⾏代码可以删了，因为记录20已经没有意义了，不会⽤20来找零
#  } else if (five >= 3) {
# five -= 3;
# twenty++; // 同理，这⾏代码也可以删了
#  } else return false;
#  }
#  }
# return true;
#  }
# };
        five=0
        ten=0
        twenty=0
        for i in bills:
            if i==5:
                five+=1
            if i ==10:
                if five<=0:
                    return False
                ten+=1
                five-=1
            if i==20:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                    twenty+=1
                elif five>=3:
                    five-=3
                    twenty+=1
                else:
                    return False
        return True


#406根据身高重建队列
class Solution:
    def reconstructQueue(self, people):
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        for p in people:
            if len(res) <= p[1]:
                res.append(p)
            elif len(res) > p[1]:
                res.insert(p[1], p)
        return res


#452最少量气球问题

class Solution:
    def findMinArrowShots(self, points):
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

# 435无重叠区域
class Solution:
    def eraseOverlapIntervals(self, intervals):
#          if (intervals.size() == 0) return 0;
#  sort(intervals.begin(), intervals.end(), cmp);
#  int count = 1; // 记录⾮交叉区间的个数
#  int end = intervals[0][1]; // 记录区间分割点
#  for (int i = 1; i < intervals.size(); i++) {
#  if (end <= intervals[i][0]) {
#  end = intervals[i][1];
#  count++;
#  }
#  }
#  return intervals.size() - count;
#  }
# };
        if len(intervals)==0:
            return 0
        intervals.sort(key=lambda x:x[1])
        result=1
        pos=intervals[0][1]
        for i in intervals:
            if pos<=i[0]:
                result+=1
                pos=i[1]
        return len(intervals)-result

#763划分字母子区间
class Solution:
    def partitionLabels(self, S):
        #         int hash and set[27] = {0}; // i为字符，hash and set[i]为字符出现的最后位置
        # for (int i = 0; i < S.size(); i++) { // 统计每⼀个字符最后出现的位置
        # hash and set[S[i] - 'a'] = i;
        #  }
        # vector<int> result;
        # int left = 0;
        # int right = 0;
        # for (int i = 0; i < S.size(); i++) {
        # right = max(right, hash and set[S[i] - 'a']); // 找到字符出现的最远边界
        # if (i == right) {
        # result.push_back(right - left + 1);
        # left = i + 1;
        #  }
        #  }
        # return result;
        #  }
        # };
        last = [0] * 26
        for i, ch in enumerate(S):
            last[ord(ch) - ord("a")] = i

        partition = list()
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1

        return partition


# 56合并区间
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        result=[]
        for i in intervals:
            if not result or result[-1][1]<i[0]:
                result.append(i)
            else:
                result[-1][1]=max(result[-1][1],i[1])
        return result

        # intervals.sort(key=lambda x: x[0])
        # merged = []
        # for interval in intervals:
        #     # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        #     if not merged or merged[-1][1] < interval[0]:
        #         merged.append(interval)
        #     else:
        #         # 否则的话，我们就可以与上一区间进行合并
        #         merged[-1][1] = max(merged[-1][1], interval[1])

        # return merged



#738单调递增数字

#监控二叉树

