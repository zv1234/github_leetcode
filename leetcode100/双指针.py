'''
双指针主要用于遍历数组，两个指针指向不同的元素，从而协同完成任务。也可以延伸到多个数组的多个指针。
若两个指针指向同一数组，遍历方向相同且不会相交，则也称为滑动窗口（两个指针包围的区域即为当前的窗口），
经常用于区间搜索。若两个指针指向同一数组，但是遍历方向相反，则可以用来进行搜索，待搜索的数组往往是排好序的。
题目类型：
        双指针
        快慢指针
        滑动窗口
'''

# 167两数之和
# 在一个增序的整数数组里找到两个数，使它们的和为给定值。已知有且只有一对解。
'''
双指针，已知为增序数组，一个从前往后，一个从后往前
'''


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [-1, -1]


# 88给定两个有序数组，把两个数组合并为一个。请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
'''
数学问题：：两增序数列合并
双指针 
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        nums1_copy = nums1
        nums1 = []
        while i < m and j < n:
            if nums1_copy[i] < nums2[j]:
                nums1.append(nums1_copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        if i < m:
            nums1[i + j:] = nums1_copy[i:]
        if j < n:
            nums1[i + j:] = nums2[j:]
        return nums1


# 142给定一个链表，如果有环路，找出环路的开始点。给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null
'''
快慢指针：fast 与slow都是从head开始，slow走一步，fast走两步，最终两者会在有环中相遇，
当fast与slow指针相遇的时候 2slow=fast 距离公式：0-环头a，环头-相遇点b  相遇点到环头c
slow走的距离（a+b)   fast 走的距离 a+n(b+c)+b
a=c+(n-1)(b+c)
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        # fast结束则没有环
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            ## 有环
            if slow is fast:
                ## 相遇处结点meetNode
                meetNode = slow
                start = head
                while start != meetNode:
                    start, meetNode = start.next, meetNode.next
                return meetNode
        return None


# 76给定两个字符串S和T，求S中包含T所有字符的最短连续子字符串的长度，同时要求时间复杂度不得超过O(n)。
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
'''
①不断增加 right 使滑动窗口增大，直到窗口包含了字符串 t 的所有元素；
②不断增加 left 使滑动窗口缩小，因为是要求最小字串，所以将不必要的元素排除在外，使长度减小，直到碰到一个必须包含的元素，这个时候不能再扔了，再扔就不满足条件了，记录此时滑动窗口的长度，并保存最小值；
③让 left 再增加一个位置，这个时候滑动窗口肯定不满足条件了，那么继续从①开始执行，寻找新的满足条件的滑动窗口，如此反复，直到j超出了字符串S范围。
'''
import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):
            # t中元素个数
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]

    def my_min(self, s, t):
        need = {}  # t 中字符个数转化为dict
        window = {}  # 记录窗口数据
        # 初始化需要的结果字典
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1
        # need={"A":1,"B":2}

        left, right = 0, 0  # 两个指针
        valid = 0  # 记录有多少个符合t字符串的字符进入到了窗口中
        start, lenght = 0, float("inf")  # 初始化结果， start 表示字串开始，lenght表示最短子串个数
        while (right < len(s)):
            s_str = s[right]
            right += 1
            if s_str not in window:
                window[s_str] = 1
            else:
                window[s_str] += 1
            if s_str in need:
                if window[s_str] == need[s_str]:  # windows 中记录的个数与need 中记录的个数相等，说明这个字符已经满足条件
                    valid += 1
                    # 当valid == len(need) 之后开始left 开始右移动，减小窗口
            while (valid == len(need)):

                if right - left < lenght:  # 记录字串起始位置与长度
                    start = left
                    lenght = right - left

                d = s[left]
                left += 1  # left 右移
                if d in need:
                    if (window[d] == need[d]):  # 如果移出去的字符刚好符合need 则left 右移后字串不符合条件。
                        valid -= 1
                    window[d] -= 1  # 在窗口中将移出去的字符数减1
        return "" if lenght == float("inf") else s[start:lenght + start]

    def my_min(self, s, t):
        need = {}  # t 中字符个数转化为dict
        window = {}  # 记录窗口数据
        # 初始化需要的结果字典
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1
        # need={"A":1,"B":2}

        left, right = 0, 0  # 两个指针
        valid = 0  # 记录有多少个符合t字符串的字符进入到了窗口中

        start, lenght = 0, float("inf")  # 初始化结果， start 表示字串开始，lenght表示最短子串个数
        while right < len(s):
            s_str = s[right]
            right += 1
            if s_str not in window:
                window[s_str] = 1
            else:
                window[s_str] += 1
                # windows 中记录的个数与need 中记录的个数相等，说明这个字符已经满足条件
            if s_str in need:
                if window[s_str] == need[s_str]:
                    valid += 1

                    # 当valid == len(need) 之后开始left 开始右移动，减小窗口
            while valid == len(need):
                if right - left < lenght:
                    # 记录字串起始位置与长度
                    start = left
                    lenght = right - left
                d = s[left]
                # left 右移
                left += 1
                if d in need:
                    # 如果移出去的字符刚好符合need 则left 右移后字串不符合条件。
                    if window[d] == need[d]:
                        valid -= 1
                    # 在窗口中将移出去的字符数减1
                    window[d] -= 1

            return "" if lenght == float("inf") else s[start:lenght + start]

# 633.SumofSquareNumbers(Easy)TwoSum题目的变形题之一。给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l,r=0,int(c**0.5)
        while l<=r:
            if l*l+r*r==c:
                return True
            elif l*l+r*r<c:
                l+=1
            else:
                r-=1
        return False

#680ValidPalindromeII(Easy)TwoSum题目的变形题之二
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len (s):
            pass



if __name__ == '__main__':
    num1 = [1, 2, 3, 0, 0, 0]
    m = 3
    num2 = [2, 5, 6]
    n = 3
    s = "ADOBECODEBANC"
    t = "ABC"
    a = Solution()
    a.minWindow(s, t)
    print(a.merge(num1, m, num2, n))
