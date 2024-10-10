class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and stack[-1] * asteroids[i] < 0:
                if abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop(-1)
                    continue
                elif abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop(-1)
                break
            else:
                stack.append(asteroids[i])
        return stack
        

if __name__=="__main__":
    s = Solution()
    test = [81,2,2,-80]
    print(s.asteroidCollision(test))