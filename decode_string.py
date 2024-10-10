class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                curr_string = ""
                while stack[-1] != '[':
                    curr_string = stack.pop() + curr_string
                stack.pop()

                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num 
                
                curr_string = int(curr_num)*curr_string
                stack.append(curr_string)
        return "".join(stack)
    

if __name__=="__main__":
    s = Solution()
    test = "3[a2[c]]"
    print(s.decodeString(test))