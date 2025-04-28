class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        res = 0
        left = 0
        last_min = -1
        last_max = -1
        
        for right in range(len(nums)):
            num = nums[right]
            if num < minK or num > maxK:
                left = right + 1
                last_min = -1
                last_max = -1
            else:
                if num == minK:
                    last_min = right
                if num == maxK:
                    last_max = right
                if last_min != -1 and last_max != -1:
                    res += min(last_min, last_max) - left + 1
        return res