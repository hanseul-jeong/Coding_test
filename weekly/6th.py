def solution(weights, head2head):
    import heapq as hq
    n_boxers = len(weights)
    # [이긴 횟수, 총 경기 수, 자기보다 무거운 복서를 이긴 횟수]
    grades = {i:[0,0,0] for i in range(n_boxers)}
    boxers = []
    # 전적계산
    for i in range(n_boxers):
        for j in range(i+1,n_boxers):
            if head2head[i][j] == 'N':continue
            win, lose = i, j
            if head2head[i][j] == 'L':
                win, lose = lose, win
            grades[win][0]+=1
            grades[win][1]+=1
            grades[lose][1]+=1
            if weights[win] < weights[lose]:
                grades[win][2] +=1
        # ( 승률 [이긴횟수/전체 경기 수], 무거운 복서를 이긴 횟수, 몸무게, 번호 ) 
        hq.heappush(boxers, (0 if not grades[i][1] else -grades[i][0]/grades[i][1], -grades[i][2], -weights[i], i))
    return [hq.heappop(boxers)[-1]+1 for _ in range(n_boxers)]
