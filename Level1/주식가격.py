"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
"""

def solution(prices):
    prices_n = len(prices)
    answer = [0]*prices_n
    for pivot in range(prices_n):
        for cmp in range(pivot+1 , prices_n):
            answer[pivot] += 1
            if prices[pivot] > prices[cmp] :
                break
    return answer
