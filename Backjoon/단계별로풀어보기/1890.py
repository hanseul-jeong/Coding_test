'''
문제
N×N 게임판에 수가 적혀져 있다. 이 게임의 목표는 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 점프를 해서 가는 것이다.

각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미한다. 반드시 오른쪽이나 아래쪽으로만 이동해야 한다. 0은 더 이상 진행을 막는 종착점이며, 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야 한다. 한 번 점프를 할 때, 방향을 바꾸면 안 된다. 즉, 한 칸에서 오른쪽으로 점프를 하거나, 아래로 점프를 하는 두 경우만 존재한다.

가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 이동할 수 있는 경로의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 게임 판의 크기 N (4 ≤ N ≤ 100)이 주어진다. 그 다음 N개 줄에는 각 칸에 적혀져 있는 수가 N개씩 주어진다. 칸에 적혀있는 수는 0보다 크거나 같고, 9보다 작거나 같은 정수이며, 가장 오른쪽 아래 칸에는 항상 0이 주어진다.

출력
가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 문제의 규칙에 맞게 갈 수 있는 경로의 개수를 출력한다. 경로의 개수는 263-1보다 작거나 같다.
'''


import sys
import heapq as hq
n = int(sys.stdin.readline())
maps =[ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
n_ways = [[0 for _ in range(n)] for __ in range(n)]
# (priority, x, y)
q = [(0,0,0)]
hq.heapify(q)
n_ways[0][0] = 1
while q:
    _, x, y = hq.heappop(q)
    if (x,y) == (n-1, n-1): continue
    k = maps[x][y]
    if not k: continue
    for dx, dy in [(1,0), (0,1)]:
        next_x, next_y = x+(k*dx), y+(k*dy)
        if next_x >n-1 or next_y >n-1: continue
        if not n_ways[next_x][next_y]:
            hq.heappush(q, (next_x+next_y, next_x, next_y))
        n_ways[next_x][next_y] += n_ways[x][y]
print(n_ways[n-1][n-1])

