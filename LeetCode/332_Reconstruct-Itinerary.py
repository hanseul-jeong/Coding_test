'''
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # find route in an ascending order
        tickets.sort()
        visited = []
        def dfs(prev, lefts):
            # if the route is founded,
            if visited : return
            if not lefts:
                visited.append(prev)
                return
            cur_des = prev[-1][-1]
            for ix in range(len(lefts)):
                # right ticket
                if cur_des == lefts[ix][0]:
                    dfs(prev + [lefts[ix]], lefts[:ix] + lefts[ix+1:])
            return
        for ix in range(len(tickets)):
            # start with the ticket of which departure is 'JFK'
            if tickets[ix][0] == 'JFK':
                dfs([tickets[ix]], tickets[:ix] + tickets[ix+1:])
        # make route from tickets (t1:(st, ed), t2:(st, ed), ..., tt(st, ed), tt(ed, st) )
        # -> (t1:(st), t2(st), ..., tt(st), tt(ed))
        return [st for st, ed in visited[0] + [visited[0][-1][::-1]]]
