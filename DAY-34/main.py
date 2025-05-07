import heapq

class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        n, m = len(moveTime), len(moveTime[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        min_time = [[float('inf')] * m for _ in range(n)]
        min_time[0][0] = 0
        heap = [(0, 0, 0)] 

        while heap:
            time, x, y = heapq.heappop(heap)

            if (x, y) == (n - 1, m - 1):
                return time

            if time > min_time[x][y]:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    next_time = time + 1
                    if next_time <= moveTime[nx][ny]:
                        next_time = moveTime[nx][ny] + 1
                    if next_time < min_time[nx][ny]:
                        min_time[nx][ny] = next_time
                        heapq.heappush(heap, (next_time, nx, ny))
