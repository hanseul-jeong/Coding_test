def minimumSwaps(arr):
    from collections import deque
    arr = deque(arr)
    n_swaps = 0
    idx = 1
    while arr:
        piv = arr.popleft()
        if piv == idx:
            idx += 1
            continue
        ix = piv-idx-1
        piv, arr[ix] = arr[ix], piv
        n_swaps += 1
        if piv != idx:
            arr.appendleft(piv)
        else:
            idx += 1
    return n_swaps
