# I improve previous version, but it still exceeds time limit at 1 case.
def freqQuery(queries):
    from collections import defaultdict
    data = defaultdict(int)
    output = []
    for q in queries:
        if q[0] == 1:
            data[q[1]] += 1
        elif q[0] == 2:
            if data[q[1]] <= 1:
                data.pop(q[1])
            else:
                data[q[1]] -= 1
        else:
            z = q[1] in data.values()
            output.append(int(z))
    return output

# previous version. It exceeds time limit
def freqQuery(queries):
    from collections import deque, defaultdict
    data = defaultdict(int)
    output = []
    queries = deque(queries)
    while queries:
        q = queries.popleft()
        if q[0] == 1:
            data[q[1]] += 1
        elif q[0] == 2:
            data[q[1]] = 0 if data[q[1]] <= 1 else data[q[1]]-1
        else:
            z = q[1] in data.values()
            output.append(int(z))
    return output
