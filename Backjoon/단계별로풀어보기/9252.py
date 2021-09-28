'''
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.
'''

import sys

word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()

dp = ['']*(len(word2)+1)
for n in range(1, len(word1)+1):
    prev = ['']
    for k in range(1, len(word2)+1):
        prev.append(prev[k-1])
        if word1[n-1] == word2[k-1] and len(prev[k]) < len(dp[k-1])+1:
            prev[k] = dp[k-1] + word1[n-1]
        elif len(prev[k]) < len(dp[k]):
            prev[k] = dp[k]
    dp = prev
print(len(dp[-1]))
if len(dp[-1]):
    print(dp[-1])

