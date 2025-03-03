class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def minMeetingRooms(intervals):
        
        if not intervals:
            return 0
            
        sortedMeetings = sorted(intervals, key=lambda x: x[0])

        paths = []
        visited = set()

        paths.append([sortedMeetings[0]])
        visited.add(sortedMeetings[0])


        for i in range(1, len(sortedMeetings)):
            for path in paths:
                if path[-1][-1] <= sortedMeetings[i][0]:
                    path.append(sortedMeetings[i])
                    visited.add(sortedMeetings[i])
                    break

            if sortedMeetings[i] not in visited:        
                paths.append([sortedMeetings[i]])
                visited.add(sortedMeetings[i])

        return len(paths)