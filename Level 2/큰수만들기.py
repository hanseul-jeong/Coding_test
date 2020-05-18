# test 10 제한시간 초과 ###########################################
# def get_max(str):
#     max_idx = 0
#     for v, idx in zip(str, range(len(str))):
#         if v > str[max_idx]:
#             max_idx = idx
#     return max_idx
# def solution(number, k):
#     digit = len(number) - k
#     answer = ""
#     while True:
#         max_idx = get_max(number[:min(k+1, len(number))])
#         answer += number[max_idx]
#         digit -= 1
#         k -= max_idx
#         if digit<=0:
#             return answer
#         elif k <= 0:
#             return answer + number[max_idx+1:]
#         number = number[max_idx+1:]


# 시간 제한 초과로 실패 ######################################

# def solution(number, k):
#     from itertools import combinations
#     import heapq as hp
#     candidates = [-int("".join(c)) for c in combinations(number,len(number)-k)]
#     hp.heapify(candidates)
#     return str(-candidates[0])
# def solution(number, k):
#     from itertools import combinations
#     candidates = list(combinations([number[i] for i in range(len(number))],len(number)-k))
#     candidates = sorted([int("".join(c)) for c in candidates ], reverse=True)
#     return str(candidates[0])
"""
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
"""
