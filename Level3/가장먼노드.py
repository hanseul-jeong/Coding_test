'''
n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
'''
from collections import deque, Counter

def bfs(st, n, graph):
    stack = deque([[st,0]])
    checked = [0 for _ in range(n+1) ]
    max_ = 0
    cnts = 0
    while stack:
        idx, cnt = stack.popleft()
        if max_ < cnt:
            max_ = cnt
            cnts = 1
        else:
            cnts+=1    
        for g in graph[idx]:
            if checked[g] or g == 1: continue
            stack.append([g, cnt+1])
            checked[g] = cnt+1      # stack에 넣을 때, 바로 check하면 stack을 따로 검사해야하는 비용 감소
    return cnts

def solution(n, edge):
    graph = {}
    for i, j in edge:
        if i not in graph.keys():
            graph[i] = []
        if j not in graph.keys():
            graph[j] = []
        graph[i].append(j)
        graph[j].append(i)

    return bfs(1, n, graph)


# previous version.

from collections import deque, Counter

def bfs(st, n, graph):
    stack = deque([[st,0]])
    checked = [0 for _ in range(n+1)]
    max_ = 0
    cnts = 0
    while stack:
        idx, cnt = stack.popleft()
        checked[idx] = cnt
        if max_ < cnt:
            max_ = cnt
            cnts = 1
        else:
            cnts+=1    
        for g in graph[idx]:
            if checked[g] or g == 1 or g in list(map(lambda x:x[0], stack)): continue
            stack.append([g, cnt+1])
    return cnts

def solution(n, edge):
    graph = {}
    for i, j in edge:
        if i not in graph.keys():
            graph[i] = []
        if j not in graph.keys():
            graph[j] = []
        graph[i].append(j)
        graph[j].append(i)

    return bfs(1, n, graph)

    # return sum([1 if l == max_ else 0 for l in lengths])
