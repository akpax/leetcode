class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = {}
        count = 0

        for row in grid:
            rows[str(row)] = rows.get(str(row),0) + 1
        
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            count += rows.get(str(col),0)
        
        return count
    
if __name__=="__main__":
    s = Solution()
    test = [[3,2,1],[1,7,6],[2,7,7]]
    print(s.equalPairs(test))

        