class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {'}': '{', ']': '[', ')': '('}
        stack = []
        for bracket in s:
            if bracket in bracketMap:
                topEle = stack.pop() if stack else None
                if bracketMap[bracket] != topEle:
                    return False
            else:
                stack.append(bracket)
        return True if not stack else False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid('['))
