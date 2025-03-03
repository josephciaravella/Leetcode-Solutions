class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


    def canAttendMeetings(intervals):
        sortedMeetings = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(sortedMeetings)):
            if sortedMeetings[i-1].end > sortedMeetings[i].start:
                return False

        return True