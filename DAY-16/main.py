class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        count = 0
        n = len(arr)

        for j in range(1, n - 1):
            valid_i = []
            for i in range(j):
                if abs(arr[i] - arr[j]) <= a:
                    valid_i.append(i)

            valid_k = []
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    valid_k.append(k)

            for i in valid_i:
                for k in valid_k:
                    if abs(arr[i] - arr[k]) <= c:
                        count += 1

        return count
