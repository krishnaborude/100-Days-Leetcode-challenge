class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_occurrence = {char: index for index, char in enumerate(s)}
        
        partitions = [] 
        partition_start = 0 
        max_reach = 0  
        
        for index, char in enumerate(s):
            max_reach = max(max_reach, last_occurrence[char]) 
            
            if index == max_reach:
                partitions.append(max_reach - partition_start + 1)  
                partition_start = index + 1
        
        return partitions
