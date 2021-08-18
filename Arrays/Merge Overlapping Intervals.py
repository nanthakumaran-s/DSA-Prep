class Solution:
    def mergeIntervals(self, intervals):
        mergedIntervals = []
        if len(intervals) == 0:
            return mergedIntervals

        tempInt = intervals[0]
        for interval in intervals:
            if interval[0] <= tempInt[1]:
                tempInt[1] = max(interval[1], tempInt[1])
            else:
                mergedIntervals.append(tempInt)
                tempInt = interval
        mergedIntervals.append(tempInt)
        return mergedIntervals

if __name__ == "__main__":
    intervals = [
        [1, 5],
        [3, 6],
        [5, 8],
        [9, 10],
        [10, 13],
    ]
    print(Solution().mergeIntervals(intervals))