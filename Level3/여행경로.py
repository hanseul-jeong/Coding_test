routes= []  # available routes
import copy 
def find_route(airport, lefts, itinerary): # recursive for finding itinerary
    global routes
    if not lefts:           # matched
        routes.append(itinerary)
        return 
    destinations = lefts.get(airport)
    if not destinations:    # not matched
        return 
    for idx in range(len(destinations)):    # destination set
        dest = destinations.pop(idx)    # choose destination
        if not destinations:    # same airport doesn't exist
            del lefts[airport]
        else:                   # renewal left tickets
            lefts[airport] = destinations
            destinations = destinations[:idx] + [dest] + destinations[idx:] # origin tickets (+ deleted tickets)
        find_route(dest, copy.deepcopy(lefts), itinerary + [dest])
def solution(tickets):
    lefts = {}
    for dep, arr in tickets:    # change tickets {departure : arrival}
        if not lefts.get(dep):
            lefts[dep] = [arr]
        else:
            lefts[dep].append(arr)
    find_route("ICN", copy.deepcopy(lefts), ["ICN"])
    # find min route in ascending order
    global routes
    import numpy as np
    routes = np.array(routes)
    (col, row) = np.shape(routes)
    candidates = list(range(col))   # idx of candidate route
    for idx_row in range(1, row):
        min = routes[candidates[0],idx_row]
        tmp = [candidates[0]]
        for idx_col in candidates[1:]:
            cand = routes[idx_col, idx_row]
            if min > cand:
                tmp = [idx_col]
                min = cand
            elif min == cand:
                tmp.append(idx_col)
        candidates = tmp
        if len(tmp) == 1:
            break
    return routes[candidates][0].tolist()

    # left의 값이 계속 변하는 까닭에 deepcopy를 이용했다.
    # 값 복사를 계속하다보니 비효율적인 것 같은데 이를 해결할 수 있는 방안은?

    """
    여행경로
  문제 설명
  주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.

  항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

  제한사항
  모든 공항은 알파벳 대문자 3글자로 이루어집니다.
  주어진 공항 수는 3개 이상 10,000개 이하입니다.
  tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
  주어진 항공권은 모두 사용해야 합니다.
  만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
  모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
"""
