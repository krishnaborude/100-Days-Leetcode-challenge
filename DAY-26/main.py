from collections import defaultdict
class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_distinct = len(set(nums))
        
        left = 0
        count = 0
        freq = defaultdict(int) 
        distinct_in_window = 0

        for right in range(len(nums)):
            if freq[nums[right]] == 0:
                distinct_in_window += 1
            freq[nums[right]] += 1

            while distinct_in_window == total_distinct:
                count += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct_in_window -= 1
                left += 1

        return count

