class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr_vowel_count = 0
        vowels = list('aeiou')
        max_vowel_count = 0
        for i in range(len(s)):
            if i >=k:
                if s[i-k] in vowels:
                    curr_vowel_count -= 1
            if s[i] in vowels:
                curr_vowel_count += 1
            max_vowel_count = max(max_vowel_count, curr_vowel_count)
        return max_vowel_count
        