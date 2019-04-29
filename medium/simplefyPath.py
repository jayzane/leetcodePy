class Solution:
    def simplifyPath(self, path: str) -> str:
        markMap = {'/': '/', '.': '.'}
        stack = []
        for s in path:
            if s in markMap:
                topEle = stack.pop() if stack else None
                if topEle != markMap[s]:
                    if topEle:
                        stack.append(topEle)
                    stack.append(s)
                elif not stack and topEle == '.':
                    pass
            elif s == '.' and stack:
                pass
            else:
                stack.append(s)
        if len(stack) > 0 and stack[-1] == '/':
            stack.pop()
        return ''.join(stack)


class SolutionB(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = [i for i in path.split('/') if i]
        path2 = []
        for i in path:
            if i in ['.']:
                continue
            elif i == '..':
                if len(path2) > 0:
                    path2.pop()
            else:
                path2.append(i)
        return '/' + '/'.join(path2)


if __name__ == '__main__':
    sol = SolutionB()
    print(sol.simplifyPath('/a//b////c/d//././/..'))
