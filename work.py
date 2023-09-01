
def minimum_value(nums):
    answer = 0
    minval=nums[0]
    for i in range(len(nums)):
        if minval>=nums[i]:
            minval=nums[i]
    answer=minval
    return answer
# [23, 20, 73, 98, 11, 4, 288]
print(minimum_value([23, 20, 73, 98, 11, 4, 288]))
