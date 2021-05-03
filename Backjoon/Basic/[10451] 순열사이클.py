'''
1부터 N까지 정수 N개로 이루어진 순열을 나타내는 방법은 여러 가지가 있다. 예를 들어, 8개의 수로 이루어진 순열 (3, 2, 7, 8, 1, 4, 5, 6)을 배열을 이용해 표현하면  															  와 같다. 또는, Figure 1과 같이 방향 그래프로 나타낼 수도 있다.

순열을 배열을 이용해  									  로 나타냈다면, i에서 πi로 간선을 이어 그래프로 만들 수 있다.

Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클" 이라고 한다.

N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.
'''

import sys

n_test = int(sys.stdin.readline())
for _ in range(n_test):
    n = int(sys.stdin.readline())
    graph = {g: i+1 for i, g in enumerate(list(map(int, sys.stdin.readline().split())))}
    dones = []
    def dfs(i, graph):
        if i in dones:
            return
        dones.append(i)
        dfs(graph[i], graph)
    cnt = 0
    for i in range(1, n+1):
        q = []
        if i in dones:continue
        dfs(i, graph)
        cnt += 1
    print(cnt)

