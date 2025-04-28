class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0] * 37  

        for i in range(1, n + 1):
            s = 0
            num = i
            while num > 0:
                s += num % 10
                num //= 10
            count[s] += 1

        max_size = max(count)
        return count.count(max_size)
