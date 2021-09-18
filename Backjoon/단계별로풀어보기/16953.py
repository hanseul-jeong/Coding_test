'''
문제
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
'''


import sys
from collections import defaultdict, deque
a, b = map(int, sys.stdin.readline().split())
q = deque([(a, 1)])
nums = defaultdict(int)
nums[a] = 1
while q:
    n, cnt = q.popleft()
    if n == b:
        break
    for next_n in [n * 2, int(str(n) + '1')]:
        if next_n <= b and not nums[next_n]:
            nums[next_n] = cnt + 1
            q.append((next_n, cnt + 1))
print(nums[b] if nums[b] else -1)
