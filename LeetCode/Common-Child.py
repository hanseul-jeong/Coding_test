# It exceeds time limit
def commonChild(s1, s2):
    n = len(s1)
    commons = [[0] * (n+1)]
    for i in range(1, n+1):
      commons.append([0])
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                commons[i].append(commons[i-1][j-1]+1)
            else:
                commons[i].append(max(commons[i-1][j], commons[i][j-1]))
    return commons[-1][-1]
