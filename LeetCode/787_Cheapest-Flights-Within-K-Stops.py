'''
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = {i:[] for i in range(n)}
        for st, ed, prc in flights:
            heapq.heappush(edges[st], (prc, ed))

        queue = deque([[0, -1, src]])    # total price, n_stops, node
        prices = [-1] * n
        paths = []
        while queue:
            top_prc, n_stops, top_ed = queue.popleft()
            if n_stops >k: continue
            if top_ed == dst:
                heapq.heappush(paths, top_prc)  # get shortest
                continue
            if prices[top_ed] != -1 and prices[top_ed] <= top_prc: continue
            prices[top_ed] = top_prc
            for prc, ed in edges[top_ed]:
                queue.append([top_prc + prc, n_stops+1, ed])
        return -1 if len(paths) == 0 else heapq.heappop(paths)
