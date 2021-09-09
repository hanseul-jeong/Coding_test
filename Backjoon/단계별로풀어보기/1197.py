'''
문제
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

입력
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
'''


# Kruskal algorithm
import sys
import heapq as hq

v, e = map(int, sys.stdin.readline().split())
parents = [i for i in range(v+1)]

def find(node):
    if node == parents[node]: return node
    return find(parents[node])

def union(n1, n2):
    a = find(n1)
    b = find(n2)
    if a == b: return None
    to_node, from_node = a, b
    if a > b:
        from_node, to_node = to_node, from_node
    # therefore, to_node < from_node
    parents[from_node] = to_node
    return None

edges = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    if b < a: a,b = b,a
    hq.heappush(edges, (c,a,b))
sum_w = 0
while edges:
    weight, n1, n2 = hq.heappop(edges)
    if find(n1) != find(n2):
        union(n1, n2)
        sum_w += weight
        if sum([parents[i] for i in range(1, v+1)]) == v: break
print(sum_w)
