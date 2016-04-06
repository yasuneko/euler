def answer(intervals):
    if len(intervals) == 1:
        start, end = intervals[0]
        return end - start
    else:
        intervals = sorted(intervals)
        i = 0
        while i < len(intervals) - 1:
            first_start, first_end = intervals[i]
            second_start, second_end = intervals[i + 1]
            if first_end < second_start:
                i += 1
            elif first_end < second_end:
                intervals[i] = first_start, second_end
                intervals.pop(i + 1)
            else:
                intervals.pop(i + 1)
        total = 0
        for interval in intervals:
            start, end = interval
            total += end - start
        return total


print answer([[1, 3], [3, 6]])
print answer([[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]])
print answer([[10, 14], [10, 13], [11, 12], [11, 13]])

print answer([[10, 14], [10, 13], [20, 22], [21, 24]])
