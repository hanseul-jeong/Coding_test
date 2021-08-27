def solution(price, money, count):
    return max(((1 + count)/2 * count * price) - money, 0)
