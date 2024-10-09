class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i in range(0,len(nums)):
            right_sum -= nums[i]
            if i != 0:
                left_sum +=nums[i-1]
            
            if left_sum == right_sum:
                return i
        return -1