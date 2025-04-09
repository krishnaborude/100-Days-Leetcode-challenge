class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if any(num < k for num in nums):
            return -1

        greater_than_k = set()
        for num in nums:
            if num > k:
                greater_than_k.add(num)

        return len(greater_than_k)
