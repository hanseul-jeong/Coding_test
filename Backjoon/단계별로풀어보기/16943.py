'''
문제
두 정수 A와 B가 있을 때, A에 포함된 숫자의 순서를 섞어서 새로운 수 C를 만들려고 한다. 즉, C는 A의 순열 중 하나가 되어야 한다. 

가능한 C 중에서 B보다 작으면서, 가장 큰 값을 구해보자. C는 0으로 시작하면 안 된다.

입력
첫째 줄에 두 정수 A와 B가 주어진다.

출력
B보다 작은 C중에서 가장 큰 값을 출력한다. 그러한 C가 없는 경우에는 -1을 출력한다.
'''


import sys
import heapq as hq
from itertools import permutations

a, b = sys.stdin.readline().split()
a, b = [n for n in a], int(b)
cands = list(set(-int(''.join(p)) for p in permutations(a, len(a)) if p[0] != '0'))
hq.heapify(cands)
answer = -1
while cands:
    v = hq.heappop(cands)
    if -v >= b: continue
    answer = -v
    break
print(answer)



