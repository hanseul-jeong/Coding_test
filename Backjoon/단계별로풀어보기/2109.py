'''
문제
한 저명한 학자에게 n(0 ≤ n ≤ 10,000)개의 대학에서 강연 요청을 해 왔다. 각 대학에서는 d(1 ≤ d ≤ 10,000)일 안에 와서 강연을 해 주면 p(1 ≤ p ≤ 10,000)만큼의 강연료를 지불하겠다고 알려왔다. 각 대학에서 제시하는 d와 p값은 서로 다를 수도 있다. 이 학자는 이를 바탕으로, 가장 많은 돈을 벌 수 있도록 순회강연을 하려 한다. 강연의 특성상, 이 학자는 하루에 최대 한 곳에서만 강연을 할 수 있다.

예를 들어 네 대학에서 제시한 p값이 각각 50, 10, 20, 30이고, d값이 차례로 2, 1, 2, 1 이라고 하자. 이럴 때에는 첫째 날에 4번 대학에서 강연을 하고, 둘째 날에 1번 대학에서 강연을 하면 80만큼의 돈을 벌 수 있다.

입력
첫째 줄에 정수 n이 주어진다. 다음 n개의 줄에는 각 대학에서 제시한 p값과 d값이 주어진다.

출력
첫째 줄에 최대로 벌 수 있는 돈을 출력한다.
'''


import sys
import heapq as hq

N = int(sys.stdin.readline())
MAX_DAY, plans = 1, []
for i in range(N):
    p, d = map(int, sys.stdin.readline().split())
    hq.heappush(plans, (-d, -p))
    MAX_DAY = max(d, MAX_DAY)

salary, tmp, day = 0, [], MAX_DAY
while plans and day >=1:
    d, p = hq.heappop(plans)
    if -d > day:
        hq.heappush(tmp, p)
    elif -d == day:
        if tmp:
            tp = hq.heappop(tmp)
            salary += -min(tp, p)
            hq.heappush(tmp, max(tp, p))
        else:
            salary += -p
        day -= 1
    else:
        hq.heappush(plans, (d,p))
        salary += 0 if not tmp else -hq.heappop(tmp)
        day -= 1
for d in range(day):
    if not tmp: break
    salary += -hq.heappop(tmp)
print(salary)


