'''
문제 설명
계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

아래 그림은 m = 4, n = 3 인 경우입니다.

image0.png

가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

제한사항
격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
물에 잠긴 지역은 0개 이상 10개 이하입니다.
집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.
입출력 예
m	n	puddles	return
4	3	[[2, 2]]	4
'''

# I reduce time complexity (dp)
def solution(m, n, puddles):
    puddles = list(map(lambda x:[x[1], x[0]], puddles))
    import heapq
    heapq.heapify(puddles)
    puddle = [0,0] if not puddles else heapq.heappop(puddles)

    def check_puddles(i, j):
        nonlocal puddle
        if [i+1, j+1] == puddle:
            if puddles:
                puddle = heapq.heappop(puddles)
            return True
        return False

    dp = [[[1, 0]]]
    for j in range(1, m):
        if check_puddles(0, j):
            dp[0].append([-1, n*m])
        else:
            dp[0].append([dp[0][j-1][0], dp[0][j-1][1]+1])
    for i in range(1, n):
        if check_puddles(i, 0):
            dp.append([[-1, n*m]])
        else:
            dp.append([[dp[i-1][0][0], dp[i-1][0][1]+1]])

        for j in range(1, m):
            # except puddle
            if check_puddles(i, j):
                dp[i].append([-1, n*m])
                continue
            dp[i].append([dp[i-1][j][0], dp[i-1][j][1]+1])
            # new shortest case
            if dp[i][j][1] > dp[i][j-1][1]+1:
                dp[i][j] = [ dp[i][j-1][0], dp[i][j-1][1]+1]
            # add-up shortest case
            elif dp[i][j][1] == dp[i][j-1][1]+1:
                dp[i][j][0] += dp[i][j-1][0]
    return dp[-1][-1][0] % 1000000007 if dp[-1][-1][0] > 0 else 0


# previous version (dp)
def solution(m, n, puddles):
    # (count, minimum route)
    dp = [[[0, m * n] for __ in range(m)] for _ in range(n)]
    for j, i in puddles:
        dp[i - 1][j - 1] = [-1, -1]
    dp[0][0] = [1, 0]
    for i in range(n):
        for j in range(m):
            for di, dj in [(1, 0), (0, 1)]:
                # except puddle or range exceeded cases
                if i + di >= n or j + dj >= m or dp[i][j][0] < 0 or dp[i + di][j + dj][0] < 0:
                    continue
                # new shortest case
                if dp[i][j][1] + 1 < dp[i + di][j + dj][1]:
                    dp[i + di][j + dj][0] = dp[i][j][0]
                    dp[i + di][j + dj][1] = dp[i][j][1] + 1
                # add-up shortest case
                elif dp[i][j][1] + 1 == dp[i + di][j + dj][1]:
                    dp[i + di][j + dj][0] += dp[i][j][0]
    return dp[-1][-1][0] % 1000000007
  
  
  # 점화식
  # if dp[i-1][j] < dp[i][j-1]: dp[i][j] = dp[i-1][j]
  # elif dp[i][j-1] < dp[i-1][j]: dp[i][j] = dp[i][j-1]
  # else: dp[i-1][j] == dp[i][j-1]: dp[i][j] = dp[i-1][j] + dp[i][j-1]
  
# dfs, it exceeds time limit
from collections import defaultdict
answers = defaultdict(int)
def add_route(position, trial, m, n, puddles):
    global answers
    if position == [m,n]:
        answers[trial] += 1
        return 1
    else:
        width, height = position
        if [width+1, height] not in puddles and width+1 <=m:
            add_route([width+1, height], trial+1, m, n, puddles)
        if [width, height+1] not in puddles and height+1 <=n:
            add_route([width, height+1], trial+1, m, n, puddles)
        return 1
def solution(m, n, puddles):
    add_route([1,1], 0, m, n, puddles)
    global answers
    answer = answers[min(answers.keys())] % 1000000007
    return answer
