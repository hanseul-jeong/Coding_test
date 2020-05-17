"""
숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다. 게임해보기

각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. 그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.

* 숫자는 맞지만, 위치가 틀렸을 때는 볼
* 숫자와 위치가 모두 맞을 때는 스트라이크
* 숫자와 위치가 모두 틀렸을 때는 아웃
예를 들어, 아래의 경우가 있으면

A : 123
B : 1스트라이크 1볼.
A : 356
B : 1스트라이크 0볼.
A : 327
B : 2스트라이크 0볼.
A : 489
B : 0스트라이크 1볼.
이때 가능한 답은 324와 328 두 가지입니다.

질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.

제한사항
질문의 수는 1 이상 100 이하의 자연수입니다.
baseball의 각 행은 [세 자리의 수, 스트라이크의 수, 볼의 수] 를 담고 있습니다.
"""

def get_result(answer, question):
    a = answer
    q = question
    strike = [0]*3
    for idx, i in enumerate([100, 10, 1]):
        if (a//i) == (q//i):
            strike[idx] = 1
        a %= i
        q %= i
    ball = 0
    for idx, n in enumerate(str(question)):
        if n in str(answer):
            if strike[idx] == 0:
                ball += 1
    return sum(strike), ball

def solution(baseball):
    from itertools import permutations
    candidates =[int("".join(map(str, tuple))) for tuple in list(permutations(range(1,10),3))]
    for question in baseball:
        true_s = question[1]
        true_b = question[2]
        drop_ele = []
        for candidate in candidates:
            st, ba = get_result(question[0], candidate)
            if (st != true_s) or (ba != true_b):
                drop_ele.append(candidate)
        for drop in drop_ele:
            candidates.remove(drop)
    return len(candidates)
