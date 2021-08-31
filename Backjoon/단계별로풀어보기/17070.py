'''
문제
유현이가 새 집으로 이사했다. 새 집의 크기는 N×N의 격자판으로 나타낼 수 있고, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 각각의 칸은 빈 칸이거나 벽이다.

오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 파이프는 아래와 같은 형태이고, 2개의 연속된 칸을 차지하는 크기이다.



파이프는 회전시킬 수 있으며, 아래와 같이 3가지 방향이 가능하다.



파이프는 매우 무겁기 때문에, 유현이는 파이프를 밀어서 이동시키려고 한다. 벽에는 새로운 벽지를 발랐기 때문에, 파이프가 벽을 긁으면 안 된다. 즉, 파이프는 항상 빈 칸만 차지해야 한다.

파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 파이프는 밀면서 회전시킬 수 있다. 회전은 45도만 회전시킬 수 있으며, 미는 방향은 오른쪽, 아래, 또는 오른쪽 아래 대각선 방향이어야 한다.

파이프가 가로로 놓여진 경우에 가능한 이동 방법은 총 2가지, 세로로 놓여진 경우에는 2가지, 대각선 방향으로 놓여진 경우에는 3가지가 있다.

아래 그림은 파이프가 놓여진 방향에 따라서 이동할 수 있는 방법을 모두 나타낸 것이고, 꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.



가로



세로



대각선

가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다. 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수를 구해보자.
'''

# DP
import sys
N = int(sys.stdin.readline())
dev = {'hor':(0,1,'hor'),'ang':(1,1,'ang'),'ver':(1,0,'ver')}
house = []
dp = [[{'hor':0, 'ang':0, 'ver':0} for _ in range(N+1)]]
for x in range(N):
    house.append(list(map(int, sys.stdin.readline().split())))
    dp.append([{'hor':0, 'ang':0, 'ver':0} for _ in range(N+1)])

dp[1][2]['hor'] = 1

for x in range(1, N+1):
    for y in range(1, N+1):
        if (x, y) in [(1, 1), (1, 2)]: continue
        if not house[x-1][y-1]:
            dp[x][y]['hor'] = dp[x][y-1]['hor'] + dp[x][y-1]['ang']
            dp[x][y]['ver'] = dp[x-1][y]['ver'] + dp[x-1][y]['ang']
            if not (house[x-2][y-1] or house[x-1][y-2]):
                dp[x][y]['ang'] = dp[x-1][y-1]['hor'] + dp[x-1][y-1]['ang'] + dp[x-1][y-1]['ver']

print(sum(list(dp[N][N].values())))


# It exceeds time limit
import sys
from collections import deque
N = int(sys.stdin.readline())
dev = {'hor':(0,1,'hor'),'ang':(1,1,'ang'),'ver':(1,0,'ver')}
house = []
for x in range(N):
    house.append(list(map(int, sys.stdin.readline().split())))

def move(x, y, st):
    if st == 'hor': # hor
        actions = ['hor', 'ang']
    elif st == 'ang':   # ang
        actions = ['hor', 'ver', 'ang']
    else:   # ver
        actions = ['ver', 'ang']
    moved = []
    for dx, dy, dst in [dev[a] for a in actions]:
        if x+dx >= N or y+dy >= N: continue
        # angular touched 2 blocks more
        if dst == 'ang' and (house[x+1][y] or house[x][y+1]): continue
        if not house[x+dx][y+dy]:
            moved.append((x+dx, y+dy, dst))
    return moved
queue = deque([(0,1,'hor')])   # x, y, stance (1:horizontal, 2: angular, 3: vertical)
answer = 0
while queue:
    x, y, st = queue.popleft()
    if (x, y) == (N-1, N-1):
        answer += 1
        continue
    queue.extend(move(x, y, st))
print(answer)
