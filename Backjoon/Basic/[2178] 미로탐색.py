'''
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
'''
import sys
from collections import deque
def isChecked(y, x, n, m, stack, maps):
    if (0<= y < n) and (0<= x < m):
        if [y, x] not in list(map(lambda x:x[:2], stack)):
            if maps[y][x] == 1 and [y, x] != [0, 0]:
                return True
    return False

def bfs(st, n, m, maps):
    stack = deque([[st[0], st[1], 1]])    # y, x, cnt
    while stack:
        coord = stack.popleft()
        maps[coord[0]][coord[1]] = coord[2]
        if coord[0] == n-1 and coord[1] == m-1:
            break
        for i, j in zip([1,0,-1,0], [0,1,0,-1]):
            new_y = coord[0]+i
            new_x = coord[1]+j
            if isChecked(new_y, new_x, n, m, stack, maps):    # Only [0,0] can be 1
                stack.append([new_y, new_x, coord[2]+1])
    return maps

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, (sys.stdin.readline().rsplit()[0]))) for _ in range(n)]

maps = bfs([0,0], n, m, maps)
print(maps[n-1][m-1])




# 시간초과.... -> stack에 넣을 때 이미 stack에 있는지 확인해야함

import sys
from collections import Counter, deque
def bfs(st, n, m, maps):
    stack = deque([[st[0], st[1], 1]])    # y, x, cnt
    while stack:
        coord = stack.popleft()
        maps[coord[0]][coord[1]] = coord[2]
        if coord[0] == n-1 and coord[1] == m-1:
            break
        for i, j in zip([1,0,-1,0], [0,1,0,-1]):
            new_y = min(max(coord[0]+i, 0), n-1)
            new_x = min(max(coord[1]+j, 0), m - 1)
            if (maps[new_y][new_x] == 1) and [new_y,new_x] != [0,0]:    # Only [0,0] can be 1
                stack.append([new_y, new_x, coord[2]+1])
    return 1

n, m = map(int, sys.stdin.readline().split())

maps = [list(map(int, (sys.stdin.readline().rsplit()[0]))) for _ in range(n)]

bfs([0,0], n, m, maps)
print(maps[n-1][m-1])

