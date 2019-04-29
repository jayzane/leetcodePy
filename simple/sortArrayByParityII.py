class Solution:
    def sortArrayByParityII(self, A):
        for n, a in enumerate(A):
            if (a - n) % 2 != 0:
                i = n + 1
                while i < len(A):
                    if (A[i] - i) % 2 != 0:
                        A[n] = A[i]
                        A[i] = a
                        break
                    i += 2
        return A

class SolutionB:
    def sortArrayByParityII(self, A):
        even = []
        odd = []
        res = []
        for a in A:
            if a & 1 == 0:
                even.append(a)
            else:
                odd.append(a)
        zip_list = zip(even, odd)
        for e, o in zip_list:
            res.extend([e, o])
        return res
if __name__ == '__main__':
    sol = Solution()
    a = [4, 2, 5, 7]
    print(sol.sortArrayByParityII(a))
