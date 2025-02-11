"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted([(i.start, i.end) for i in intervals])

        for i in range(1, len(sorted_intervals)):
            last = sorted_intervals[i -1]
            curr = sorted_intervals[i]
            if curr[0] < last[1]:
                return False
            last_meeting_end = curr[1]
        else:
            return True
