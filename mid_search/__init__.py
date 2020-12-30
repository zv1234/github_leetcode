#while 循环和递归写二分查找

# 二分法模版
def mind(nums,target):
    star=0
    end=len(nums)-1
    while star+1<end:
        #防止溢出
        mid=star+(end-star)/2
        if nums[mid]==target:
            end=mid
        elif nums[mid]<target:
            star=mid
        else:
            end=mid
    if nums[star]==target:
        return star
    if nums[end]==target:
        return end
    return -1


