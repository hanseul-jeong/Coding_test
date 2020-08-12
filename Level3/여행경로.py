routes= []
def find_route(airport, lefts, itinerary):
    if not lefts:
        global routes
        routes.append(itinerary + [airport])
        return
    destinations = lefts.get(airport)
    if not destinations:
        return
    for idx in range(len(destinations)):
        dest = destinations.pop(idx)
        if not destinations:
            del lefts[airport]
        else:
            lefts[airport] = destinations
            destinations = destinations[:idx] + [dest] + destinations[idx:]
        find_route(dest, lefts, itinerary + [dest])
def solution(tickets):
    lefts = {}
    for dep, arr in tickets:
        if not lefts.get(dep):
            lefts[dep] = [arr]
        else:
            lefts[dep].append(arr)
    tmp_lefts = lefts.copy()
    destinations = tmp_lefts.get("ICN")
    for idx in range(len(destinations)):
        tmp_list = destinations.copy()
        dest = tmp_list.pop(idx)
        if not tmp_list:
            del tmp_lefts["ICN"]
        else:
            tmp_lefts["ICN"] = tmp_list
        print(tmp_lefts)
        find_route(dest, tmp_lefts, ["ICN"] + [dest])
    global routes
    # import numpy as np
    # routes = np.array(routes)
    # (col, row) = np.shape(routes)
    # candidates = range(1, col)
    # for idx_row in range(1, row):
    #     min = routes[0,idx_row]
    #     for idx_col in candidates:
    #         cand = routes[idx_col, idx_row]
    #         if min > cand:
    #             candidates = [idx_col]
    #             min = cand
    #         elif min == cand:
    #             candidates.extend(idx_col)
    #     if len(candidates) == 1:
    #         break
    # print(candidates)
    return 0
    # return routes[candidates[0]]
    
    
    # dict의 값이 왜 변하는지 잘 모르겠다... python도 주소참조여서 그런가??ㅜㅜ
    # 확인!!!!!!!!!!!!!!!!!!!!!!!!
    
    
    
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
