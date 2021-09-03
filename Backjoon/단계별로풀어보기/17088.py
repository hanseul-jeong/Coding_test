'''
문제
크기가 N인 수열 A = [A1, A2, ..., AN]이 있을 때, 모든 1 ≤ i < N에 대해서, Ai+1-Ai가 모두 일치하면 등차수열이라고 한다. 예를 들어, [3], [6, 6, 6], [2, 8, 14, 20], [6, 4, 2]는 등차수열이고, [4, 5, 4], [6, 3, 1]은 등차수열이 아니다.

수열 B = [B1, B2, ..., BN]을 등차수열로 변환하려고 한다. 각각의 수에는 연산을 최대 한 번 적용할 수 있다. 연산은 두 가지가 있는데, 1을 더하거나 1을 빼는 것이다. 수열 B를 등차수열로 변환하기 위해 필요한 연산 횟수의 최솟값을 구해보자.

입력
첫째 줄에 수열 B의 크기 N(1 ≤ N ≤ 105)이 주어진다. 둘째 줄에는 B1, B2, ..., BN(1 ≤ Bi ≤ 109)이 주어진다.

출력
수열 B를 등차수열로 변화시키기 위한 연산 횟수의 최솟값을 출력한다. 등차수열로 변환시킬 수 없다면 -1을 출력한다.
'''


import sys

n = int(sys.stdin.readline().rstrip())
min_cnt = n+1
# all permutations of operation
targets = [(di, dj) for di, dj in [(0,0), (1,1), (-1,-1),
                                   (1,0), (0,1), (-1,0),
                                   (0,-1), (1,-1), (-1,1)]]
# exception
if not n or n==1: 
    min_cnt = 0
    targets = None
nums = list(map(int, sys.stdin.readline().split()))
while targets:
    di, dj = targets.pop()
    target = nums[1]+di - (nums[0]+dj)
    cnt = abs(di) + abs(dj)
    p = nums[1]+di
    for ix in range(2, n):
        diff = abs(target - (nums[ix] - p))
        if diff > 1:
            cnt = n+1
            break
        cnt += diff
        p += target
        if cnt >= min_cnt: break
    min_cnt = min(min_cnt, cnt)
print(-1 if min_cnt == n+1 else min_cnt)
