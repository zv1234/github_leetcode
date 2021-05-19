#encoding:utf-8

# 77给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
class Solution:
    def combine(self, n: int, k: int) :
        result = []
        path = []
        #递归参数
        def backtrack(start, n, k):
            #递归出口
            if len(path) == k:
                result.append(path[:])
                return
            #单层递归逻辑   #剪枝
            for i in range(start, n - (k - len(path)) + 1):
                path.append(i)
                backtrack(i + 1, n, k)
                path.pop()

        backtrack(1, n + 1, k)
        return result

# 216找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
class Solution:
    def combinationSum3(self, k: int, n: int):
        reslut=[]
        path=[]
        def backstrack(targetsum,k,Sum,index):
            if len(path)==k and targetsum==Sum:
                reslut.append(path[:])
                return
            for i in range(index,10):
                Sum+=i
                path.append(i)
                backstrack(targetsum,k,Sum,i+1)
                Sum-=i
                path.pop()
        backstrack(n,k,0,1)
        return reslut

    # 减枝操作
    '''
    reslut=[]
        path=[]
        def backstrack(targetsum,k,Sum,index):
            if Sum>targetsum:
                return
            if len(path)==k and targetsum==Sum:
                reslut.append(path[:])
                return 
            for i in range(index,11-k+len(path)):
                Sum+=i
                path.append(i)
                backstrack(targetsum,k,Sum,i+1)
                Sum-=i
                path.pop()
        backstrack(n,k,0,1)
        return reslut
    '''

#39给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        def backstrack(candidates,target,Sum,startindex):
            if Sum>target:
                return
            if Sum==target:
                result.append(path[:])
            for i in range(startindex,len(candidates)):
                Sum+=candidates[i]
                path.append(candidates[i])
                # 不⽤i + 1了，表示可以重复读取当前的数
                backstrack(candidates,target,Sum,i)
                Sum-=candidates[i]
                path.pop()
        backstrack(candidates,target,0,0)
        return result
