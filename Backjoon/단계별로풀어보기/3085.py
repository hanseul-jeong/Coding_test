'''
문제
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

출력
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
'''


# greedy
import sys
N, candies = int(sys.stdin.readline()), []
for _ in range(N):
    candies.append(str(sys.stdin.readline().rstrip()))

n_candy = 1
def get_sec_candy(arr):
    global n_candy
    cur, max_n, curr_n  = arr[0], 1, 1
    for i in range(1, N):
        if arr[i] == cur:
            curr_n += 1
        else:
            max_n = max(max_n, curr_n)
            cur, curr_n = arr[i], 1
    if max(max_n, curr_n) > n_candy:
        n_candy = max(max_n, curr_n)

for x in range(N):
    get_sec_candy(candies[x])
    if n_candy == N: break
    for y in range(N):
        get_sec_candy([candies[i][y] for i in range(N)])

        if x+1 <= N-1 and candies[x][y] != candies[x+1][y]:
            get_sec_candy([candies[x+1][i] if i != y else candies[x][i] for i in range(N)])
            get_sec_candy([candies[x][i] if i != y else candies[x+1][i] for i in range(N)])
            # (i-x+1)%2+x == x -> x+1 / x+1 -> x
            get_sec_candy([candies[i][y] if i in [x,x+1] else candies[(i-x+1)%2+x][y] for i in range(N)])

        if y+1 <= N-1 and candies[x][y] != candies[x][y+1]:
            get_sec_candy([candies[i][y+1] if i != x else candies[x][y] for i in range(N)])
            get_sec_candy([candies[i][y] if i != x else candies[x][y+1] for i in range(N)])
            # (i-y+1)%2+y == y -> y+1 / y+1 -> y
            get_sec_candy([candies[x][i] if i in [y,y+1] else candies[x][(i-y+1)%2+y] for i in range(N)])
print(n_candy)
