'''
기숙사 생활을 하는 학교에서 어떤 금요일(전원 귀가일)에는 모두 집으로 귀가를 한다.

오랜만에 집에 간 영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 생각해 보다가
"바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다.

바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
'''

import sys

n_stone = int(sys.stdin.readline())

maps = list(map(lambda x:[0] * 19, range(19)))

for n in range(n_stone):
    x, y = map(int, sys.stdin.readline().split())
    maps[x - 1][y - 1] = 1
for n in range(19 ** 2):
    i, j = n // 19, n % 19
    print(maps[i][j], end=' ')
    if j == 19 - 1:
        print('')

