nums = [3, 5, 2, 8, 9]

def bubble_sort(nums):
    if len(nums) == 1:
        return nums
    n = len(nums)
    for i in range(n - 1, -1, -1):
        for j in range(1, i + 1):
            if nums[i] < nums[i - 1]:
                tmp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = tmp
    return nums

print(bubble_sort(nums))
print(bubble_sort([2]))
print(bubble_sort([3, 1]))
