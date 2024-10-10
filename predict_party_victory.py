class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D = []
        R = []
        n = len(senate)

        for i, senator in enumerate(senate):
            if senator == 'D':
                D.append(i)
            else:
                R.append(i)
        
        while D and R:
            if D[0] < R[0]:
                R.pop(0)
                D.append(D.pop(0)+n)
            else:
                D.pop(0)
                R.append(R.pop(0)+n)
        
        if R:
            return "Radiant" 
        else:
            return 'Dire'
