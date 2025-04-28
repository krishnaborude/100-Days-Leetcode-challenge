class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        return result