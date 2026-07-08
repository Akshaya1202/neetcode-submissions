class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == '+':
                a,b = stack[-1],stack[-2]
                stack.append(a+b)
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                a = stack[-1]
                stack.append(a*2)
            else:
                stack.append(int(i))
        summ = 0
        for i in stack:
            summ = summ + i
        return summ