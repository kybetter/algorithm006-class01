def move_zero_index(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0 :
            nums[j] = nums[i]
            if j != i:
                nums[0]
            j += 1

    return nums


def move_zero_swap(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    return nums

def move_zero(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    nums[j:] = [0]*(len(nums)-j)

    return nums