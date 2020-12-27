#encoding:utf-8
#2.1选择排序
'''
首先，找到数组中最小的那个元素，其次，将它和数组的第 一个元素交换位置（如果第一个元素就是最小元素那么它就和自己交换）。
再次，在剩下的元素中 找到最小的元素，将它与数组的第二个元素交换位置。
如此往复，直到将整个数组排序。这种方法 叫做选择排序，因为它在不断地选择剩余元素之中的最小者。
'''

def selection(nums):
    a=len(nums)
    for i in range(a):
        min=i
        for j in range(i+1,a):
            if nums[j]<nums[min]:
                min=j
        nums[i],nums[min]=nums[min],nums[i]
    return nums


#插入排序
'''
通常人们整理桥牌的方法是一张一张的来，将每一张牌插入到其他已经有序的牌中的适当位置。 
在计算机的实现中，为了给要插入的元素腾出空间，我们需要将其余所有元素在插入之前都向右移 动一位。
这种算法叫做插入排序，
'''
def insertion(nums):
    a=len(nums)
    for i in range(a):
        key=nums[i]
        #将a[i]插入到a[i-1],a[i-2],a[i-3]...中
        j=i-1
        while j>0 and key<nums[j]:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums

#2.1.6希尔排序
'''
希尔排序的思想是使数组中任意间隔为 h 的元素都是有序的。这样的数组被称为 h 有序数组。
换句话说，一个 h 有序数组就是 h 个互相独立的有序数组编织在一起组成的一个数组
'''


def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 2)
    return arr




if __name__ == '__main__':
    a=[1,2,3,6,4,9,5,10,17,11]
    print selection(a)