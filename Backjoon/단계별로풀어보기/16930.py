'''
문제
진영이는 다이어트를 위해 N×M 크기의 체육관을 달리려고 한다. 체육관은 1×1 크기의 칸으로 나누어져 있고, 칸은 빈 칸 또는 벽이다. x행 y열에 있는 칸은 (x, y)로 나타낸다.

매 초마다 진영이는 위, 아래, 오른쪽, 왼쪽 중에서 이동할 방향을 하나 고르고, 그 방향으로 최소 1개, 최대 K개의 빈 칸을 이동한다.

시작점 (x1, y1)과 도착점 (x2, y2)가 주어졌을 때, 시작점에서 도착점으로 이동하는 최소 시간을 구해보자.

입력
첫째 줄에 체육관의 크기 N과 M, 1초에 이동할 수 있는 칸의 최대 개수 K가 주어진다.

둘째 줄부터 N개의 줄에는 체육관의 상태가 주어진다. 체육관의 각 칸은 빈 칸 또는 벽이고, 빈 칸은 '.', 벽은 '#'으로 주어진다.

마지막 줄에는 네 정수 x1, y1, x2, y2가 주어진다. 두 칸은 서로 다른 칸이고, 항상 빈 칸이다.

출력
(x1, y1)에서 (x2, y2)로 이동하는 최소 시간을 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.

제한
2 ≤ N, M ≤ 1,000
1 ≤ K ≤ 1,000
1 ≤ x1, x2 ≤ N
1 ≤ y1, y2 ≤ M
'''


import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().split())
maps, visited, MAX = [], [], n*m+1
for _ in range(n):
    maps.append(list(map(str, sys.stdin.readline().rstrip())))
    visited.append([MAX for _ in range(m)])
sx, sy, dx, dy = map(int, sys.stdin.readline().split())
# adjust coordinates
sx, sy, dx, dy = sx-1, sy-1, dx-1, dy-1
dirs = [(1,0), (0,1), (-1,0), (0,-1)]
q = deque([(sx, sy)])
visited[sx][sy]= 0
while q:
    x, y = q.popleft()
    times = visited[x][y]
    for nx, ny  in dirs:
        for nk in range(1, k+1):
            next_x, next_y = x + (nk*nx), y + (nk*ny)
            # out of bounds or meet wall
            if next_x < 0 or next_x > n-1 or next_y < 0 or next_y > m-1: break
            if maps[next_x][next_y] == '#': break
            if visited[next_x][next_y] < times+1: break
            if visited[next_x][next_y] == times+1: continue
            visited[next_x][next_y] = times+1
            if (next_x, next_y) == (dx, dy): break
            q.append((next_x, next_y))

print(visited[dx][dy] if visited[dx][dy] != MAX else -1)
