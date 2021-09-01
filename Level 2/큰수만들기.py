"""
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
"""

# heapq
def solution(number, k):
    import heapq as hq
    answer, q = '', []
    cnt, left = k, 0
    for i, n in enumerate(number):
        hq.heappush(q, (-int(n), i))
        if i < left + cnt: continue
        while q:
            node, idx = hq.heappop(q)
            # removed numbers
            if idx < left: continue
            # new number
            answer += str(-node)
            k -= (idx - left)
            cnt = k
            left = idx + 1
            break
        if not k: break

    return answer + number[left:] if not k else answer

# exceeds time limit (list indexing)
def solution(number, k):
    answer = ''
    while k:
        m = max(number[:k+1])
        answer += m
        idx = number.index(m)
        number = number[idx+1:]
        k -= idx
    return answer + number

# exceeds time limit (two pointer)
def solution(number, k):
    answer = ''
    left, right = 0, 0
    pivot=0
    while k:
        if (right - pivot) == k:
            answer += number[left]
            k -= (left-pivot)
            left += 1
            right, pivot = left, left
        else:
            right += 1
            if number[left] < number[right]:
                left = right
    return answer + number[left:]

# 21.05.02 version 아직.. 시간초과로 33점

def solution(number, k):
    max_n = '0'
    numbers = [[n, i] for i, n in enumerate(number)]
    from itertools import combinations
    cands = list(combinations(numbers, len(numbers) - k))
    cands = list(set([''.join([y[0] for y in cand]) for cand in cands]))
    return str(max(map(int, cands)))

        

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

