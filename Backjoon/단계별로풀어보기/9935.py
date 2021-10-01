'''
문제
상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

폭발은 다음과 같은 과정으로 진행된다.

문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.

폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

입력
첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.

둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.

두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

출력
첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.
'''

# I checked "algoritm category" in boj
import sys
from collections import deque, defaultdict
seq = deque(map(str, sys.stdin.readline().rstrip()))
b = sys.stdin.readline().rstrip()
bomb = defaultdict(int, {b[i]:i+1 for i in range(len(b))})

left, tmp = [], []
while seq:
    ch = seq.popleft()
    if bomb[ch]:
        # first or next character
        if bomb[ch] == 1 or (tmp and bomb[tmp[-1]]+1 == bomb[ch]):
            tmp.append(ch)
        else:
            left.extend(tmp+[ch])
            tmp = []
    else:
        left.extend(tmp+[ch])
        tmp = []

    if tmp and bomb[tmp[-1]] == len(b):
        for _ in range(len(b)):
            tmp.pop()
answer = left+tmp
print('FRULA' if not answer else ''.join(answer))



# It exceeds time limit
import sys
from collections import deque


text = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()
n_text, n_pattern = len(text), len(pattern)
connected, q = [[0,1,-1]], deque([])

def get_start(t, p):
    while t >= 0:
        if p == 0:
            return t
        t, p = connected[t][0], p - 1

for i in range(1, n_text+1):
    # string connection (before, after)
    connected.append([i-1, i+1, 0])
    if text[i-1] == pattern[0]:
        q.append((i, 1))
        connected[i][-1] = 1
connected += [[n_text, n_text+1, -1]]
while q:
    i_text, i_pattern = q.popleft()
    if i_pattern == n_pattern:
        left = get_start(i_text, i_pattern)
        right = connected[i_text][1]
        connected[left][1] = right
        connected[right][0] = left
        if connected[left][-1] not in [-1, 0]:
            q.append((left, connected[left][-1]))
        continue
    ni_text = connected[i_text][1]
    if ni_text > n_text : continue
    if not connected[ni_text][-1]:
        if text[ni_text-1] == pattern[i_pattern]:
            connected[ni_text][-1] = i_pattern+1
            q.append((ni_text, i_pattern+1))
        else:
            connected[ni_text][-1] = -1
answer, start ='', connected[0][1]
while start <= n_text:
        answer += text[start-1]
        start = connected[start][1]
print('FRULA' if not answer else answer)
