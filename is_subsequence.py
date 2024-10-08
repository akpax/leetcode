class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        tp,sp = 0,0
        while sp < len(s) and tp < len(t):
            if t[tp] == s[sp]:
                sp += 1
            tp += 1
        return sp == len(s)