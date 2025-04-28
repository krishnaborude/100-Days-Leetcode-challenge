class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        N = len(nums)
        left=nums[0]
        for i in range(1,N):
            if nums[i]>left:
                left=nums[i]
                continue
            for j in range(i+1,N):
                res=max(res,(left-nums[i])*nums[j])
        return res