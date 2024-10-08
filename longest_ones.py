class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            print(f"l: {l}, r: {r}")
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r-l+1
    

if __name__=="__main__":
    s = Solution()
    test = [1,1,1,0,0,0,1,1,1,1,0]
    print(s.longestOnes(test,2))