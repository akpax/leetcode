class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        def get_elements_only_in_first_list(nums1,nums2):
            nums2_hash = {}
            for num in nums2:
                nums2_hash[num] = True
                
            onlynums1 = []
            for num in nums1:
                if not nums2_hash.get(num):
                    onlynums1.append(num)
            return set(onlynums1)

        nums1_ans = get_elements_only_in_first_list(nums1,nums2)
        nums2_ans = get_elements_only_in_first_list(nums2,nums1)

        return [nums1_ans,nums2_ans]