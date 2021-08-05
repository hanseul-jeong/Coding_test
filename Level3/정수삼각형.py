'''
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

제한사항
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.
입출력 예
triangle	result
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30
'''

def solution(triangle):
    dp = [[triangle[i][j] for j in range(i+1)] for i in range(len(triangle))]
    for i in range(1, len(triangle)):
        for j in range(i+1):
            dp[i][j] = max(dp[i-1][max(j-1, 0)], dp[i-1][min(j, i-1)]) + dp[i][j]
    return max(dp[-1])
  
# 점화식
# dp[i][j] = max(dp[i-1][j], dp[i-1][j+1]) + dp[i][j] where j >=0 j+1 <= i-1
