'''
문제
전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다.

그러나 당신의 병사들은 하얀 옷을 입고, 적국의 병사들은 파란옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다.

문제는, 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.

N명이 뭉쳐있을 때는 N^2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

입력
첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 모든 자리에는 병사가 한 명 있다. (B는 파랑, W는 흰색이다.)

출력
첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.
'''


import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
maps = [ list(map(str, sys.stdin.readline().rstrip())) for _ in range(m)]
visited = [ [0 for _ in range(n)] for __ in range(m)]
totals = {'W':0, 'B':0}
for ix in range(n*m):
    x, y = ix // n, ix % n
    if visited[x][y]: continue
    q = deque([(x, y)])
    visited[x][y], color, nums = 1, maps[x][y], 1
    while q:
        i, j = q.popleft()
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            if i+dx<0 or i+dx>m-1 or j+dy<0 or j+dy>n-1: continue
            if visited[i+dx][j+dy]: continue
            if maps[i+dx][j+dy] != color: continue
            visited[i+dx][j+dy] = 1
            nums += 1
            q.append((i+dx, j+dy))
    totals[color] += (nums**2)
print(*totals.values())
