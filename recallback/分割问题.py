#encoding:utf-8

# 131分割回文字符串
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 回文串 是正着读和反着读都一样的字符串。

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res =[]
        def isValid(s, start, end):
            if start > end:
                return False
            while start<=end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        def backtracking(s, path, idx):
            # "aab" 如果idx >= 3，说明已经找到一组分割方案
            if idx >= len(s):
                res.append(path.copy())
                return
            for i in range(idx, len(s)):
                if isValid(s, idx, i):
                    path.append(s[idx:i+1])
                    backtracking(s, path, i+1)
                    path.pop()
                else:
                    # 别break哟，比如ab不是回文，但是下一个aba是哟
                    continue
        backtracking(s, [], 0)
        return res