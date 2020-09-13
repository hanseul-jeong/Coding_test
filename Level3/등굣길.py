
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
    
'''
문제 설명
계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

아래 그림은 m = 4, n = 3 인 경우입니다.

image0.png

가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.
'''
