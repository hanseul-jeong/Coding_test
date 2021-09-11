'''
문제
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
'''


# 1. two pointer
import sys
n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
i, j, sub_s = 0, 0, nums[0]
min_l = 1 if sub_s >= s else 0
while i <= n-1:
    if sub_s < s:
        j += 1
        if j > n-1: break
        sub_s += nums[j]
        continue
    if not min_l:
        min_l = j-i+1
    else:
        min_l = min(min_l, j-i+1)
    if min_l == 1: break
    sub_s -= nums[i]
    i += 1
print(min_l)

# 2. partial sum
import sys
n, s = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(1, n+1):
    nums[i] += nums[i-1]
left, right = 0, 1
min_l = n+1
while left < n:
    if nums[right] - nums[left] < s:
        right += 1
        if right > n: break
        continue
    min_l = min(min_l, right-left)
    left+=1
if min_l == n+1: min_l = 0
print(min_l)



