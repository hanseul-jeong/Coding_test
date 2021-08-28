'''
텔레포트 3
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	512 MB	303	122	101	43.348%
문제
수빈이는 크기가 무한대인 격자판 위에 살고 있다. 격자판의 각 점은 두 정수의 쌍 (x, y)로 나타낼 수 있다.

제일 처음에 수빈이의 위치는 (xs, ys)이고, 집이 위치한 (xe, ye)로 이동하려고 한다.

수빈이는 두 가지 방법으로 이동할 수 있다. 첫 번째 방법은 점프를 하는 것이다. 예를 들어 (x, y)에 있는 경우에 (x+1, y), (x-1, y), (x, y+1), (x, y-1)로 이동할 수 있다. 점프는 1초가 걸린다.

두 번째 방법은 텔레포트를 사용하는 것이다. 텔레포트를 할 수 있는 방법은 총 세 가지가 있으며, 미리 정해져 있다. 텔레포트는 네 좌표 (x1, y1), (x2, y2)로 나타낼 수 있으며, (x1, y1)에서 (x2, y2)로 또는 (x2, y2)에서 (x1, y1)로 이동할 수 있다는 것이다. 텔레포트는 10초가 걸린다.

수빈이의 위치와 집의 위치가 주어졌을 때, 집에 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 xs와 ys가, 둘째 줄에 xe, ye가 주어진다. (0 ≤ xs, ys, xe, ye ≤ 1,000,000,000)

셋째 줄부터 세 개의 줄에는 텔레포트의 정보 x1, y1, x2, y2가 주어진다. (0 ≤ x1, y1, x2, y2 ≤ 1,000,000,000)

입력으로 주어지는 모든 좌표 6개는 서로 다르다.

출력
수빈이가 집에 가는 가장 빠른 시간을 출력한다.
'''

# It exceeds time limit
import sys
from collections import deque, defaultdict

xs, ys = map(int, sys.stdin.readline().split())
xe, ye = map(int, sys.stdin.readline().split())
m_route = abs(xe-xs) + abs(ye-ys)
print(m_route)
tels = defaultdict(tuple)
for i in range(3):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    tels[(x1, y1)], tels[(x2, y2)] = (x2, y2), (x1, y1)
grid_x = max([k[0] for k in tels.keys()] + [xs, xe]) + 1
grid_y = max([k[1] for k in tels.keys()] + [ys, ye]) + 1

visited = [[ m_route for _ in range(grid_y)] for __ in range(grid_x)]
visited[xs][ys] = 0
queue = deque([(xs, ys, 0)])
while queue:
    x, y, cnt = queue.popleft()
    if cnt > visited[xe][ye]: continue
    if tels[(x, y)]:
        new_x, new_y = tels[(x, y)]
        if visited[new_x][new_y] > cnt + 10:
            queue.append((new_x, new_y, cnt + 10))
            visited[new_x][new_y] = cnt + 10
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if x + dx < 0 or x + dx >= grid_x or y + dy < 0 or y + dy >= grid_y: continue
        if visited[x+dx][y+dy] > cnt+1:
            queue.append((x+dx, y+dy, cnt+1))
            visited[x+dx][y+dy] = cnt+1
print(visited[xe][ye])


