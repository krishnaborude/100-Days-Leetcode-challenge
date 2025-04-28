class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        if k == 1:
            return 0
        
        my_list=[]
        for i in range(len(weights)-1):
            my_list.append(weights[i] + weights[i + 1])
        
        my_list.sort()
        min_score=sum(my_list[:k-1])
        max_score=sum(my_list[-(k-1):])
        return max_score-min_score