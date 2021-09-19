'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에 어떻게 이동해야 하는지 공백으로 구분해 출력한다.
'''

# n > k의 경우 갈 수 있는 방법이 한 가지 밖에 없으므로,
# 이 부분에 대해서 따로 구해주면 시간낭비를 줄일 수 있음
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
MAX = 100000 + abs(k - n)
visited = [-1]*(MAX+1)

def backtracking(idx):
    q = [[idx]]
    while q:
        tracks = q.pop()
        idx = tracks[-1]
        if idx == n:
            print(len(tracks)-1)
            print(*(tracks[::-1]))
            return None
        q.append(tracks + [visited[idx]])
if n>=k:
    print(n-k)
    print(*[i for i in range(n, k-1, -1)])
else:
    visited[n] = n
    q = deque([n])
    while q:
        idx = q.popleft()
        if idx == k:
            backtracking(idx)
            break
        for next_idx in [idx+1, idx-1, 2*idx]:
            if next_idx < 0 or next_idx > MAX: continue
            if visited[next_idx] != -1: continue
            visited[next_idx] = idx
            q.append(next_idx)
