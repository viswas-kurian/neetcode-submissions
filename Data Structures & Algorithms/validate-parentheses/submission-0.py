class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {')':'(',']':'[','}':'{'}

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            
            else:

                if not stack:
                    return False
                
                if stack[-1]==map[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0



