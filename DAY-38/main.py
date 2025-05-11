class Solution(object):
    def threeConsecutiveOdds(self, arr):
        i, n = 0, len(arr)
        while i + 2 < n:
            if arr[i]&1 and arr[i+1] & 1 and arr[i+2] & 1:
                return True
            if not arr[i+2]&1:
                i += 3
            elif not arr[i+1]&1:
                i += 2
            else:
                i += 1
        return False