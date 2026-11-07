class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {']':'[','}':'{',')':'('}
        stack = []
        for i in s:
            if i in hmap:
                if stack and stack[-1] == hmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False