'''
문제
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다. 경우의 수는 231보다 작다.
'''

# dp
import sys
import heapq as hq
n, k = map(int, sys.stdin.readline().split())
coins_ = []
for _ in range(n):
    c = int(sys.stdin.readline())
    if c > k: continue
    hq.heappush(coins_, c)
coins= []
while coins_:
    c = hq.heappop(coins_)
    coins.append(c)
# 이전 (i-1)-th까지의 코인을 이용해서 k값을 만드는 방법의 갯수
dp_ = [1]+[0]*k
for i in range(len(coins)):
    dp = []
    for j in range(k+1):
        dp.append(dp_[j])
        if j < coins[i]: continue
        dp[j] += dp[j-coins[i]]
    dp_ = dp
print(dp_[k])

# previous version 
# brute-force (exceeds time limit)
import sys
import heapq as hq
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coin = int(sys.stdin.readline())
    if coin > k: continue
    hq.heappush(coins, coin)
n_coin = len(coins)
st = [(coins[i], i) for i in range(n_coin)]
n_cases = 0
while st:
    n_sum, idx = st.pop()
    if n_sum == k:
        n_cases += 1
        continue
    for i in range(idx, n_coin-1):
        if n_sum + coins[i] > k: break
        st.append((n_sum+coins[i], i))
    # 마지막 index인 경우
    if (k - n_sum) % coins[n_coin-1] == 0:
        st.append((k, n_coin-1))
print(n_cases)
