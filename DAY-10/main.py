class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        i = 0
        n = len(nums)

        while i < n:
            seen = set()
            has_duplicate = False

            for j in range(i, n):
                if nums[j] in seen:
                    has_duplicate = True
                    break
                seen.add(nums[j])
            
            if not has_duplicate:
                break 
            
            i += 3
            operations += 1

        return operations
