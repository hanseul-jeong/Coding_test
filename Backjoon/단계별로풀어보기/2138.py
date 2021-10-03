'''
문제
N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는(1) 상태와 꺼져 있는 (0) 상태 중 하나의 상태를 가진다. i(1<i<N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(2≤N≤100,000)이 주어진다. 다음 줄에는 전구들의 현재 상태를 나타내는 숫자 N개가 공백 없이 주어진다. 그 다음 줄에는 우리가 만들고자 하는 전구들의 상태를 나타내는 숫자 N개가 공백 없이 주어진다.

출력
첫째 줄에 답을 출력한다. 불가능한 경우에는 -1을 출력한다.
'''


import sys

n = int(sys.stdin.readline())
states = list(map(int, sys.stdin.readline().rstrip()))
dest = list(map(int, sys.stdin.readline().rstrip()))
dp =[[1] + [0 for _ in range(n-1) ],
     [0 for _ in range(n)]]
# 1. click 1st switch
dp[0][1] = int(states[0] == dest[0])
# 2. non-click 1st switch
dp[1][1] = int(states[0] != dest[0])
for i in range(2, n):
    for j in range(2):
        c = states[i-1]
        for k in range(i-2, i):
            if dp[j][k]:
                c = not c
        dp[j][i] = int(c != dest[i-1])

dp_st = [int(states[-1]), int(states[-1])]

for ix in range(n-2, n):
    for j in range(2):
        dp_st[j] = not dp_st[j] if dp[j][ix] else dp_st[j]

answers = []
for j in range(2):
    if dp_st[j] == int(dest[-1]):
        answers.append(sum(dp[j]))
print(-1 if not answers else min(answers))




