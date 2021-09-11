'''
문제
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!

입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

출력
강의실의 개수를 출력하라.
'''

# 두 개의 우선순위 큐 이용
# 1) 시작 시간으로 오름차순 정렬한 q1
# 2) q1을 pop한 값을 종료 시간으로 오름차순 정렬한 q2
import sys
import heapq as hq
n = int(sys.stdin.readline())
# q1
timetable = []
for _ in range(n):
    # start, end
    hq.heappush(timetable, tuple(map(int, sys.stdin.readline().split())))
# q2
n_class, ends = 1, []
while timetable:
    st, ed = hq.heappop(timetable)
    while ends:
        t = hq.heappop(ends)
        if t > st:
            hq.heappush(ends, t)
            break
    hq.heappush(ends, ed)
    n_class = max(len(ends), n_class)
print(n_class)
