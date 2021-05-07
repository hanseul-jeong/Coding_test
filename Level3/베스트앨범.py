"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
"""

def solution(genres, plays):
    g_imp = {k:[] for k in list(set(genres))}
    cnts = {k:0 for k in g_imp.keys()}
    for i, (g, p) in enumerate(zip(genres, plays)): # 재생 수, 순서순으로 sort / 장르 별 play 수 count
        g_imp[g] += [(-p, i)]
        cnts[g] += p
    for k in g_imp.keys():  # 생성된 리스트를 sort     => 처음부터 heapq로 구현해도 좋을듯
        g_imp[k] = sorted(g_imp[k])
    import heapq
    importance = [(-v, k) for k, v in cnts.items()]
    heapq.heapify(importance)
    ret = []
    while importance:
        genre = heapq.heappop(importance)
        ret.append(g_imp[genre[1]][0][1])
        if len(g_imp[genre[1]]) >=2:
            ret.append(g_imp[genre[1]][1][1])
        # ret.extend(list(map(lambda x:x[1], g_imp[genre[1]][:2])))
    return ret

# previous version
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
        
    return answer

