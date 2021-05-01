'''
격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
'''

import sys

n, m = list(map(int, sys.stdin.readline().split()))
stick_map = list(map(lambda x: [0] * m, range(n)))

n_stick = int(sys.stdin.readline())

for i in range(n_stick):
    st_size, direction, y, x = list(map(int, sys.stdin.readline().split()))
    x -= 1
    y -= 1
    if direction == 0:
        stick_map[y][x:x + st_size]=[1]*st_size
    else:
        for y_idx in range(y, y+st_size):
            stick_map[y_idx][x] = 1
for i in range(n):
    for j in range(m):
        print(stick_map[i][j], end=' ')
    print('')


# 2d list에서 column 참조할 때 slicing이 안된다는점...
