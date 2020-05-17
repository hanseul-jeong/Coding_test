"""
여러 개의 쇠막대기를 레이저로 절단하려고 합니다. 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자릅니다. 쇠막대기와 레이저의 배치는 다음 조건을 만족합니다.
"""

def solution(arrangement):
    sticks = 0
    answer = 0
    arrangement = arrangement.replace('()','-')
    for a in arrangement:
        if a == '(':
            sticks += 1
        else:
            if a == ')':
                answer += 1
                sticks -= 1
            else:
                answer += sticks
    return answer
