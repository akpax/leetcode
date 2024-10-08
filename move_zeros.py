class Solution:
    def moveZeroes(self, nums) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums
        
if __name__=="__main__":
    s = Solution()
    test = [0,1,0,3,12]
    print(s.moveZeroes(test))