'''
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.
'''

# 21.05.02 recursion error python에서 1000이상의 call은 error를 발생시킨다고 한다.
import sys
available = {1:[1], -1:[-1]}
def bfs(i, cnt, avb):
    cands = []
    global k, exit_cond, available
    if k == i:
        if cnt < exit_cond:
            exit_cond = cnt
        return [cnt]
    if cnt > exit_cond: return []
    for d in avb:
        cands += bfs(i+d, cnt+1, available[d])
    cands += bfs(i*2, cnt + 1, [1, -1])
    return cands

n, k = list(map(int, sys.stdin.readline().split()))

exit_cond = abs(k - n)
cands = bfs(n, 0, [1, -1])

min_minutes = exit_cond
from collections import Counter
cands = Counter(cands)
print(exit_cond)
print(cands[exit_cond])



