class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        max_window = 0
        zeros = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            max_window = max(max_window, r-l)

        return max_window