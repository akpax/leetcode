# # this code runs in 35 ms
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        num_map = {}
        for num in arr:
            if num not in num_map.keys():
                num_map[num] = 1
            else:
                num_map[num] += 1
        occurences = num_map.values()
        return len(occurences) == len(set(occurences))

# This code runs in 46 ms but feels cleaner
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        num_freq = {}
        for num in arr:
            num_freq[num] = num_freq.get(num,0) + 1
            
        occurences = num_freq.values()
        return len(occurences) == len(set(occurences))