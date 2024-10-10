class RecentCounter:

    def __init__(self):
        self.count = 0
        self.req_times = []
        

    def ping(self, t: int) -> int:
        self.req_times.append(t)
        self.count += 1
        while self.req_times and self.req_times[0] < t-3000:
            self.req_times.pop(0)
            self.count -= 1
        return self.count
