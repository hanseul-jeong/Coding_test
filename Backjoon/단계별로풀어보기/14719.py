'''
문제
2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.



비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

입력
첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)

두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.

따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

출력
2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.

빗물이 전혀 고이지 않을 경우 0을 출력하여라.
'''


import sys
def flush(tmp_b, max_l):
    rain = 0
    for b in tmp_b:
        rain += max_l - b
    return rain
h, w = map(int,sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))
max_l, tmp_b = blocks[0], [blocks[0]]
rains = 0

for b in blocks[1:]:
    if b > max_l:
        rains += flush(tmp_b, max_l)
        max_l = b
        tmp_b = [max_l]
    else:
        tmp_b.append(b)
right = 0
for b in tmp_b[::-1]:
    if right < b:
        right = b
    else:
        rains +=  right - b
print(rains)

