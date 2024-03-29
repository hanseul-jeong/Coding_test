'''
문제
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

입력
첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

출력
첫째 줄에 자연수 N의 최댓값을 출력한다.
'''


# 1부터 j까지의 총 합을 s_j라고 하면,
# s_(j-1) <= s < s_j
# (s_j - s)를 k라 하면,
# 1<= k <= j
# 따라서 1 부터 j까지의 수 중에서 k하나를 빼면 s를 만들 수 있다
import sys

s = int(sys.stdin.readline())
n_sum, j = 1, 1
while n_sum <= s:
    j += 1
    n_sum += j
print(j-1)


        
