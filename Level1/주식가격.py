"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
"""

# naive ver.
def solution(prices):
    prices_n = len(prices)
    answer = [0]*prices_n
    for pivot in range(prices_n):
        for cmp in range(pivot+1 , prices_n):
            answer[pivot] += 1
            if prices[pivot] > prices[cmp] :
                break
    return answer

'''
테스트 1 〉	통과 (140.74ms, 18.8MB)
테스트 2 〉	통과 (109.20ms, 17.7MB)
테스트 3 〉	통과 (183.43ms, 19.6MB)
테스트 4 〉	통과 (124.58ms, 18.3MB)
테스트 5 〉	통과 (88.53ms, 16.9MB)
'''


# 2021-05-01
# O(N)
def solution(prices):
    ret = [0]*len(prices)
    holdings = []
    for idx, price in enumerate(prices):
        if len(holdings) == 0:
            holdings.append([price,idx])
            continue
        while holdings:
            top = holdings[-1]
            if top[0] <= price:
                break
            out = holdings.pop()
            ret[out[1]] = idx - out[1]
        holdings.append([price, idx])
    for hold in holdings:
        ret[hold[1]] = len(prices) - (hold[1]+1)
    return ret
'''
테스트 1 〉	통과 (32.79ms, 18.7MB)
테스트 2 〉	통과 (24.11ms, 17.6MB)
테스트 3 〉	통과 (36.32ms, 19.5MB)
테스트 4 〉	통과 (27.93ms, 18.3MB)
테스트 5 〉	통과 (21.30ms, 16.9MB)
'''
