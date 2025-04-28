class Solution(object):
    def countSubarrays(self, nums):
        count = 0
        for i in xrange(len(nums) - 2):
            if (nums[i] + nums[i+2]) * 2 == nums[i+1]:
                count += 1
        return count
