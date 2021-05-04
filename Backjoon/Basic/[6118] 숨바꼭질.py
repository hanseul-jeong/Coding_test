'''
재서기는 수혀니와 교외 농장에서 숨바꼭질을 하고 있다.
농장에는 헛간이 많이 널려있고 재서기는 그 중에 하나에 숨어야 한다.
헛간의 개수는 N(2 <= N <= 20,000)개이며, 1 부터 샌다고 하자.  

재서기는 수혀니가 1번 헛간부터 찾을 것을 알고 있다.
모든 헛간은 M(1<= M <= 50,000)개의 양방향 길로 이어져 있고, 그 양 끝을 A_i 와 B_i(1<= A_i <= N; 1 <= B_i <= N; A_i != B_i)로 나타낸다.
또한 어떤 헛간에서 다른 헛간으로는 언제나 도달 가능하다고 생각해도 좋다. 

재서기는 발냄새가 지독하기 때문에 최대한 냄새가 안나게 숨을 장소를 찾고자 한다. 
냄새는 1번 헛간에서의 거리(여기서 거리라 함은 지나야 하는 길의 최소 개수이다)가 멀어질수록 감소한다고 한다. 
재서기의 발냄새를 최대한 숨길 수 있는 헛간을 찾을 수 있게 도와주자!
'''

# 노드 간 중복 연결이 가능해서 DFS로는 거리를 잴 수 없게된다.

import sys
from collections import deque
def bfs(st, graph):
    visited = {}
    queue = deque([[st, 0]])    # index, depth
    while queue:
        top = queue.popleft()
        if top[0] in visited.keys(): continue
        visited[top[0]] = top[1]
        if graph[top[0]]: queue.extend(deque([[g, top[1]+1] for g in graph[top[0]] ]))
    return visited

n, m = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = list(map(int, sys.stdin.readline().split()))
    graph[x].append(y)  # 처음에 x < y 조건으로 단방향 그래프를 만들었었는데,
    graph[y].append(x)  # 부모가 자식보다 값이 작다는 조건이 없어서 이 경우에도 오답..! 따라서 양방향 그래프로 작성해야 한다.

visited = bfs(1, graph)
max_length = max(visited.values())

cands = [k for k, v in visited.items() if v == max_length]
print('{0} {1} {2}'.format(min(cands), max_length, len(cands)))
