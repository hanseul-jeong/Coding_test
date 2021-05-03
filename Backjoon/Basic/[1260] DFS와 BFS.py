'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.
'''
import sys
from collections import deque
from functools import reduce
def dfs(st, graph):
    visited = []
    queue = deque([st])
    while queue:
        i = queue.popleft()
        if i in visited: continue
        visited.append(i)
        queue = graph[i] + queue
    return visited

def bfs(st, graph):
    visited = []
    stack = deque([st])
    while stack:
        i = stack.popleft()
        if i in visited: continue
        visited.append(i)
        stack.extend(graph[i])
    return visited

n_nodes, n_edges, st = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n_nodes+1)]
for _ in range(n_edges):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
graph = [deque(sorted(list(set(g)))) for g in graph]
print(''.join(str(dfs(st, graph))[1:-1].split(',')))
print(''.join(str(bfs(st, graph))[1:-1].split(',')))

