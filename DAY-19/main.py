from collections import defaultdict
class Solution(object):
    def countPairs(self, nums, k):
        value_indices = defaultdict(list)
        count = 0
        for idx, num in enumerate(nums):
            value_indices[num].append(idx)
        for indices in value_indices.values():
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count
