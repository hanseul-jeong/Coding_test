'''
문제
문자열과 놀기를 세상에서 제일 좋아하는 영식이는 오늘도 문자열 2개의 LCS(Longest Common Subsequence)를 구하고 있었다. 어느 날 영식이는 조교들이 문자열 3개의 LCS를 구하는 것을 보았다. 영식이도 도전해 보았지만 실패하고 말았다.

이제 우리가 할 일은 다음과 같다. 영식이를 도와서 문자열 3개의 LCS를 구하는 프로그램을 작성하라.

입력
첫 줄에는 첫 번째 문자열이, 둘째 줄에는 두 번째 문자열이, 셋째 줄에는 세 번째 문자열이 주어진다. 각 문자열은 알파벳 소문자로 이루어져 있고, 길이는 100보다 작거나 같다.

출력
첫 줄에 첫 번째 문자열과 두 번째 문자열과 세 번째 문자열의 LCS의 길이를 출력한다.
'''


import sys

word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()
word3 = sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(word3) + 1)] for __ in range(len(word2)+1)]
for n in range(1, len(word1)+1):
    prev = [[0 for _ in range(len(word3) + 1)] for __ in range(len(word2) + 1)]
    for j in range(1,len(word2)+1):
        for k in range(1, len(word3) + 1):
            prev[j][k] = max(prev[j][k-1], prev[j-1][k], dp[j][k])
            if word1[n-1] == word2[j-1] and word1[n-1] == word3[k-1]:
                prev[j][k] = max(dp[j-1][k-1] + 1, prev[j][k])
    dp = prev

print(dp[-1][-1])
