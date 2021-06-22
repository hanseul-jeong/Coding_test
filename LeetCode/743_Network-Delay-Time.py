'''
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
'''

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i:[] for i in range(1, n+1)}
        for st, ed, p in times: edges[st].append((p, ed))
        visited = [-1] * (n+1)
        queue = deque([[k, 0]])
        # start
        visited[k] = 0
        while queue:
            node, time = queue.popleft()
            for p, cand in edges[node]:
                # first or relax
                if visited[cand] == -1 or visited[cand] > time + p:
                    queue.append([cand, time + p])
                    visited[cand] = time + p
        # if all nodes are visited, get maximum time or -1
        return max(visited[1:]) if all([v!= -1 for v in visited[1:]]) else -1
