'''
문제
n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다. 가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력한다.
'''

# Reducing redundant if statements is helpful (Python3 passed)
import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    c = int(sys.stdin.readline())
    # k 초과 coin 제외
    if c > k: continue
    coins.append(c)
# 이전 (i-1)-th까지의 코인을 이용해서 j값을 만드는 방법의 갯수
dp = [[k+1]*(k+1)]
for i in range(1, len(coins)+1):
    dp.append([])
    for j in range(k+1):
        dp[i].append(dp[i-1][j])
        if j < coins[i-1]: continue
        if j == coins[i-1]: dp[i][j] = 1
        dp[i][j] = min(dp[i][j], dp[i][j-coins[i-1]]+1)
print(dp[len(coins)][k] if dp[len(coins)][k] != k+1 else -1)


# Using python3 exceeds time limit, but it can be accepted by using pypy3
import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    c = int(sys.stdin.readline())
    # k 초과 coin 제외
    if c > k: continue
    coins.append(c)
# 이전 (i-1)-th까지의 코인을 이용해서 j값을 만드는 방법의 갯수
dp = [[0]*(k+1)]
for i in range(1, len(coins)+1):
    dp.append([])
    for j in range(k+1):
        dp[i].append(dp[i-1][j])
        if j < coins[i-1]: continue
        if j == coins[i-1]: dp[i][j] = 1
        if dp[i][j-coins[i-1]]:
            # dp[i-1][j] & dp[i][j-coin[i]]
            if dp[i][j]:
                dp[i][j] = min(dp[i][j], dp[i][j-coins[i-1]]+1)
            # dp[i-1][k] == 0
            else:
                dp[i][j] = dp[i][j-coins[i-1]]+1
print(dp[len(coins)][k] if dp[len(coins)][k] else -1)
