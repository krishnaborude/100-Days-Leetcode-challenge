import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        dp = [[float('inf')] * m for _ in range(n)]
        heap = [(0, 0, 0)]  

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while heap:
            time, row, col = heapq.heappop(heap)
            if time >= dp[row][col]:
                continue
            dp[row][col] = time
            if row == n - 1 and col == m - 1:
                return time
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < n and 0 <= c < m:
                    cost = (row + col) % 2 + 1
                    wait_time = max(time, moveTime[r][c])
                    total = wait_time + cost
                    if total < dp[r][c]:
                        heapq.heappush(heap, (total, r, c))
        return -1