def minimumBribes(q):
    n_bribe = 0
    idx = len(q)
    while q:
        pos = q.pop()
        if pos != idx:
            if idx not in q[-2:]:
                print('Too chaotic')
                return -1
            ix = 1 if q[-1] == idx else 2
            del q[-ix]
            q.append(pos)
            n_bribe += ix
        idx -= 1
    print(n_bribe)
    return 0
