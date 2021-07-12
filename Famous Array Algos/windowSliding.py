'''
  Sliding Window Technique in Python
  
'''
def window(nums, k):
    curSum = 0
    for i in range(k):
        curSum += nums[i]
    maxSum = curSum
    for i in range(k, len(nums)):
        curSum += nums[i] - nums[i - k]
        maxSum = max(curSum, maxSum)
    return maxSum
