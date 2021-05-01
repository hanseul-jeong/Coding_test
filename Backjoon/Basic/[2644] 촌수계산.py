'''
우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다.
이러한 촌수는 다음과 같은 방식으로 계산된다.
기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다.
예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.
'''

import sys

def getParent(st):
    global tree
    pivot = st
    parents = []
    while True:
        if pivot not in tree.keys():
            break
        parents.append(tree[pivot])
        pivot = parents[-1]

    return parents

n_node = int(sys.stdin.readline())
i, j = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
tree = {}
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    tree[y] = x
p1, p2 = getParent(i), getParent(j)

commons = [idx for idx in [i] + p1 if idx in [j] + p2]
if commons:
    print(([i] + p1).index(commons[0]) + ([j] + p2).index(commons[0]))
else:
    print(-1)
