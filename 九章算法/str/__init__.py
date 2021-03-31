#encoding:utf-8
#344反转字符串
class Solution:
    def reverseString(self, s) :
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

#541反转字符串2
class Solution:
    def reverseStr(self, s, k):
        n = len(s)
        arr = list(s)
        for i in range(0, n, 2 * k):
            arr[i:i + k] = arr[i:i + k][::-1]
        return "".join(arr)
