'''
문제
폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.



아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.

테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

입력
첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)

둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

출력
첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
'''



# Backtracking + DFS + exception ('ㅏ')
import sys

n, m = map(int, sys.stdin.readline().split())
maps, visited, max_v = [], [], 0
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))
    visited.append([0 for _ in range(m)])
    max_v = max(max_v, max(maps[-1]))
# ㅏ,ㅓ,ㅗ,ㅜ
shapes = [[(0, 0), (1, 0), (1, 1), (2, 0)], [(0, 0), (1, 0), (1, -1), (2, 0)],
          [(0, 0), (0, 1), (-1, 1), (0, 2)], [(0, 0), (0, 1), (1, 1), (0, 2)]]
max_sum = 0


def dfs(x, y, tracks):
    global max_sum
    if len(tracks) == 4:
        max_sum = max(max_sum, sum(tracks))
        return
    if maps[x][y] + (4-len(tracks))*max_v < max_sum:
        return
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if x + dx < 0 or y + dy < 0 or x + dx > n - 1 or y + dy > m - 1: continue
        if visited[x + dx][y + dy]: continue
        visited[x + dx][y + dy] = 1
        dfs(x + dx, y + dy, tracks + [maps[x + dx][y + dy]])
        visited[x + dx][y + dy] = 0
    return

for ix in range(n * m):
    x, y = ix // m, ix % m
    # check 'ㅏ' and its variations
    for coords in shapes:
        tmp = 0
        for dx, dy in coords:
            if x + dx < 0 or x + dx > n - 1 or y + dy < 0 or y + dy > m - 1: continue
            tmp += maps[x + dx][y + dy]
        max_sum = max(max_sum, tmp)
    # check other shapes
    visited[x][y] = 1
    dfs(x, y, [maps[x][y]])
    visited[x][y] = 0
print(max_sum)
