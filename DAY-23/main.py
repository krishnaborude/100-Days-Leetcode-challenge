class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        curr =min_v =max_v = 0
        for d in differences:
            curr+=d
            if curr < min_v:
                min_v =curr
            elif curr > max_v:
                max_v = curr
        return (upper - max_v) -(lower - min_v) +1 if (upper - max_v) >= (lower - min_v)else 0
