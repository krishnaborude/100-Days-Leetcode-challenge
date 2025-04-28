class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        def is_symmetric(num_str):
            half = len(num_str) // 2
            return sum(map(int, num_str[:half])) == sum(map(int, num_str[half:]))

        count = 0
        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0 and is_symmetric(s):
                count += 1
        return count
