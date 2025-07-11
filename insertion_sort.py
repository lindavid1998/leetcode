def sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i):
            if nums[j] > nums[i]:
                tmp = nums[i]
                del nums[i]
                nums.insert(j, tmp)
    return nums

print(sort([5,3,7,8]))
print(sort([3]))
print(sort([1, 2, 3]))
