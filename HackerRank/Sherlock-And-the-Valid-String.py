def isValid(s):
    from collections import Counter
    char_dist = Counter(s)      # a : 1, b : 1, ... , e : 3
    chars = char_dist.keys()    # (a, b, ..., e)
    repeated_dist = Counter(list(char_dist.values()))   #{(1, 4), (3, 1)} (# of repeated, frequency)
    repeated = list(repeated_dist.keys())               # # of repeated
    is_valid = False
    # These cases can return YES.
    # 1) all numbers appear the same # of times
    if len(repeated) == 1: is_valid = True
    # 2) only 1 number appears one more times than others
    elif len(repeated) == 2:
        a,b = repeated
        if repeated_dist[a] > repeated_dist[b]: a, b = b, a
        # single character can be removed
        if a == 1 and repeated_dist[a] == 1:  is_valid = True
        elif a - b == 1 and repeated_dist[a] == 1:   is_valid = True
    return 'YES' if is_valid else 'NO'
