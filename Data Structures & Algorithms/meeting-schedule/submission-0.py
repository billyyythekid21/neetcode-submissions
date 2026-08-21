"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda interval: interval.start)

        for i in range(1, len(sorted_intervals)):
            prev = sorted_intervals[i - 1].end
            curr = sorted_intervals[i].start

            if curr < prev:
                return False

        return True