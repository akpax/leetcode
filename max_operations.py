class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l,r = 0, len(nums)-1
        operations = 0
        nums.sort()
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                operations += 1
                l += 1
                r -= 1
            elif s < k:
                l += 1
            else:
                r -= 1
        