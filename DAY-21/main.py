class RecentCounter(object):

    def __init__(self):
        self.requests = []
        self.start = 0

    def ping(self, t):
        self.requests.append(t)
        while self.requests[self.start] < t - 3000:
            self.start += 1
        return len(self.requests) - self.start
