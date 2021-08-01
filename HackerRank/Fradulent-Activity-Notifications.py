def activityNotifications(expenditure, d):
    if d % 2 == 0:
        def median(arr):
            return (arr[d//2] + arr[d//2 - 1]) / 2
    else:
        def median(arr): return arr[d//2]
    import bisect
    n_alarm = 0
    tmp = sorted(expenditure[:d])
    for i in range(len(expenditure)-d):
        med = median(tmp)
        if med * 2 <= expenditure[i+d]: n_alarm += 1
        index = bisect.bisect_left(tmp, expenditure[i])
        del tmp[index]
        bisect.insort(tmp, expenditure[i+d])
    return n_alarm
