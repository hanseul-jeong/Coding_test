def substrCount(n, s):
    from collections import deque
    n_special = n
    queue = deque([])
    for i in range(n-1):
        if s[i] == s[i+1]:
            n_special += 1
            queue.append((i, i+1, s[i]))
        if i < n-2 and s[i] == s[i+2]:
            n_special += 1
            queue.append((i, i+2, s[i]))
    while queue:
        x, y, char = queue.popleft()
        new_x, new_y = x-1, y+1
        if new_x < 0 or new_y > n - 1: continue
        if s[new_x] == s[new_y] and s[new_x] == char:
            n_special += 1
            queue.append((new_x, new_y, char))
    return n_special
