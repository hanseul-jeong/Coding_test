'''
문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''

import sys

N, M = map(int, sys.stdin.readline().split())
inputs = list(map(int, sys.stdin.readline().split()))
# inputs.sort()
n_cases = 0
left, right = 0, 1
while True:
    if left == N: break
    if sum(inputs[left:right]) == M:  # count
        n_cases += 1
    if sum(inputs[left:right]) >= M or right == N:  # overflow
        left += 1
    else:   # underflow
        right += 1
print(n_cases)
