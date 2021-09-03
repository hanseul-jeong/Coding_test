'''
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
이를 사전순으로 정렬하면 다음과 같이 된다.

1+1+1+1
1+1+2
1+2+1
1+3
2+1+1
2+2
3+1
정수 n과 k가 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법 중에서 k번째로 오는 식을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 n과 k가 주어진다. n은 양수이며 11보다 작고, k는 231-1보다 작거나 같은 자연수이다.

출력
n을 1, 2, 3의 합으로 나타내는 방법 중에서 사전 순으로 k번째에 오는 것을 출력한다. k번째 오는 식이 없는 경우에는 -1을 출력한다.
'''


import sys
n, k = map(int, sys.stdin.readline().split())
dp = [['1'], ['1+1','2'], ['1+1+1', '1+2','2+1','3']]


for i in range(3, n):
    tmp = [st + '+1' for st in dp[-1]]
    tmp += [st + '+2' for st in dp[-2]]
    tmp += [st + '+3' for st in dp[-3]]
    dp.append(tmp)

if k > len(dp[n-1]): print(-1)
else:
    import heapq as hq
    hq.heapify(dp[n-1])
    for _ in range(k-1):
        hq.heappop(dp[n-1])
    print(hq.heappop(dp[n-1]))
