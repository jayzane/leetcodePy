class Solution:
    def sortString(self, s: str) -> str:
        array = [ord(s1) for s1 in s]
        res = []
        bs = [0 for _ in range(26)]
        start_o = ord('a')
        for a in array:
            bs[a - start_o] += 1
        while len(res) < len(array):
            for i in range(26):
                if bs[i]:
                    res.append(i + start_o)
                    bs[i] -= 1

            for i in range(25, -1, -1):
                if bs[i]:
                    res.append(i + start_o)
                    bs[i] -= 1
        sorted()
        return ''.join(map(lambda x: chr(x), res))

    def sortString0(self, s: str) -> str:
        # 错误
        def bd_big(d, root, end):
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and d[child + 1] > d[child]:
                    child += 1
                if d[child] > d[root]:
                    d[child], d[root] = d[root], d[child]
                    root = child
                else:
                    break

        def bd_small(d, root, end):
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and d[child + 1] < d[child]:
                    child += 1
                if d[child] < d[root]:
                    d[child], d[root] = d[root], d[child]
                    root = child
                else:
                    break

        def get_small(d):
            l = len(d)
            if l <= 1:
                return d, []
            root = (l - 1) // 2
            for i in range(root, -1, -1):
                bd_small(d, root, l - 1)
            res = []
            for i in range(l - 1, 0, -1):
                if res and d[0] <= res[-1]:
                    break
                else:
                    res.append(d[0])
                    d[i], d[0] = d[0], d[i]
                    d.pop()
                    bd_small(d, 0, i - 1)
            return res, d

        def get_big(d):
            l = len(d)
            if l <= 1:
                return d, []
            root = (l - 1) // 2
            for i in range(root, -1, -1):
                bd_big(d, root, l - 1)
            res = []
            for i in range(l - 1, 0, -1):
                if res and d[0] >= res[-1]:
                    break
                else:
                    res.append(d[0])
                    d[i], d[0] = d[0], d[i]
                    d.pop()
                    bd_big(d, 0, i - 1)
            return res, d

        res = []
        arr = [s1 for s1 in s]
        while arr:
            res_small, arr = get_small(arr)
            res_big, arr = get_big(arr)
            res.extend(res_small)
            res.extend(res_big)
        return ''.join(res)

    def sortString2(self, s: str) -> str:

        def sort_func1(d, asc):
            l = len(d)
            for i in range(l):
                for j in range(l - i - 1):
                    if (asc and d[j] > d[j + 1]) or (not asc  and d[j] < d[j + 1]):
                        d[j], d[j + 1] = d[j + 1], d[j]
            return d

        def sort_desc1(d, asc):
            l = len(d)
            for i in range(l):
                for j in range(l - i - 1):
                    if d[j] < d[j + 1]:
                        d[j], d[j + 1] = d[j + 1], d[j]
            return d

        def sort_func2(data, asc):
            # 快速
            def qs(d, low, high):
                if low < high:
                    pi = part(d, low, high)
                    qs(d, low, pi - 1)
                    qs(d, pi + 1, high)

            def part(d, low, high):
                i = low
                p = d[high]
                for j in range(low, high):
                    if (asc and d[j] < p) or (not asc and d[j] > p):
                        d[i], d[j] = d[j], d[i]
                        i += 1
                d[i], d[high] = d[high], d[i]
                return i

            qs(data, 0, len(data) - 1)
            return data

        def sort_func3(data, asc):
            minv = min(data)
            maxv = max(data)
            tmp = [0 for _ in range(maxv - minv + 1)]
            res = [0 for _ in range(len(data))]
            if asc:
                index_f = lambda x: x - minv
            else:
                index_f = lambda x: maxv - x
            for i in data:
                try:
                    tmp[index_f(i)] += 1
                except Exception as e:
                    pass
            for i in range(1, len(tmp)):
                tmp[i] += tmp[i - 1]
            for i in data:
                res[tmp[index_f(i)] - 1] = i
                tmp[index_f(i)] -= 1
            return res

        def sort(res, arr, asc=True):
            if len(arr) <= 1:
                res.extend(arr)
                return arr, []
            tmp = []
            arr = sort_func3(arr, asc)
            last_val = None
            for a in arr:
                if last_val != a:
                    res.append(a)
                    last_val = a
                else:
                    tmp.append(a)
            return sort(res, tmp, not asc)

        array = [ord(s1) for s1 in s]
        result = []
        sort(result, array, asc=True)
        return ''.join(map(lambda x: chr(x), result))

    def sortString3(self, s: str) -> str:
        def sort_func3(data, asc):
            minv = min(data)
            maxv = max(data)
            tmp = [0 for _ in range(maxv - minv + 1)]
            res = [0 for _ in range(len(data))]
            if asc:
                index_f = lambda x: x - minv
            else:
                index_f = lambda x: maxv - x
            for i in data:
                tmp[index_f(i)] += 1
            for i in range(1, len(tmp)):
                tmp[i] += tmp[i - 1]
            for i in data:
                res[tmp[index_f(i)] - 1] = i
                tmp[index_f(i)] -= 1
            return res

        def sort(arr):
            arr = sort_func3(arr, asc=False)
            res = []
            while arr:
                last_val = None
                tmp = []
                while arr:
                    a = arr.pop()
                    if last_val != a:
                        res.append(a)
                        last_val = a
                    else:
                        tmp.append(a)
                arr = tmp
            return res

        array = [ord(s1) for s1 in s]
        result = sort(array)
        return ''.join(map(lambda x: chr(x), result))

if __name__ == '__main__':
    sol = Solution()
    s = 'aaaabbbbcccc'
    s = 'leetcode'
    res1 = sol.sortString(s)
    print(res1)
