    
  """
  단어 변환
문제 설명
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 hit, target가 cog, words가 [hot,dot,dog,lot,log,cog]라면 hit -> hot -> dot -> dog -> cog와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
"""



# 21.05.05 오히려 이전 버전보다 느림.
# 왜 previous가 더 빠르지..?
from collections import deque

def getChangeable(w, words):
    cands = []
    for word in words:
        if sum([0 if w[i] == word[i] else 1 for i in range(len(w))]) == 1: cands.append(word)
    return cands

# def getChangeable(w, words):
#     cands = []
#     for word in [w_ for w_ in words if w_ != w]:
#         for i in range(len(w)):
#             if w[:i] == word[:i] and w[i+1:] == word[i+1:]:
#                 cands.append(word)
#                 break
#     return cands
def bfs(st, ed, graph):
    checked = {k:0 for k in graph.keys()}
    stack = deque([[st, 0]])
    while stack:
        top = stack.popleft()
        k, v = top
        checked[k] = v if k != st else -1
        if k == ed: break
        for c in graph[k]:
            if checked[c] or c in list(map(lambda x:x[0], stack)) : continue
            stack.append([c, v+1])
    return checked

def solution(begin, target, words):
    if target not in words:
        return 0
    graph = {w:getChangeable(w, words) for w in set([begin] + words)}
    checked = bfs(begin, target, graph)
    return checked[target]


# previous version.
answer = []
def find(word, lefts, target, cnt):
    global answer
    candidates = [left for left in lefts if sum([ 1 if w != l else 0 for w, l in zip(word, left)])==1]
    if not candidates:
        return 0
    if target in candidates:
        answer.append(cnt+1)
        return cnt+1
    for c in candidates:
        find(c, [l for l in lefts if l not in candidates], target, cnt+1)
        
def solution(begin, target, words):
    if target not in words:
        return 0
    find(begin, words, target, 0)
    global answer
    if answer:
        return min(answer)
    return 0
    
  # 한 글자씩 변환할 때마다 left에서 지운 후 다시 탐색
  # 시간 면에서 효율적이지 못함
