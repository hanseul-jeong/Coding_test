'''
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
'''

# DP
import sys
N = int(sys.stdin.readline())
dp = [N] * (N+1)
dp[0], dp[1] = 0, 0
for i in range(2, N+1):
    tmp = N
    if (i%3) == 0:
        tmp = dp[i//3]+1 if tmp > dp[i//3]+1 else tmp
    if (i%2) == 0:
        tmp = dp[i//2]+1 if tmp > dp[i//2]+1 else tmp
    tmp = dp[i-1] + 1 if tmp > dp[i-1] + 1 else tmp
    dp[i] = tmp
print(dp[N])


# exceeds time limit
import sys
from collections import deque
def op(node, cnt):
    cands = []
    if node % 3 == 0:
        cands.append((node // 3, cnt+1))
    if node % 2 == 0:
        cands.append((node // 2, cnt+1 ))
    cands.append((node - 1, cnt+1))
    return cands
N = int(sys.stdin.readline())

q = deque([(N, 0)])
answer = N
while q:
    node, cnt = q.popleft()
    if node == 1:
        answer = answer if answer < cnt else cnt
        break
    q.extend(op(node, cnt))
print(answer)
