'''
문제
상근이가 1학년 때, 덧셈, 뺄셈을 매우 좋아했다. 상근이는 숫자가 줄 지어있는 것을 보기만 하면, 마지막 두 숫자 사이에 '='을 넣고, 나머지 숫자 사이에는 '+' 또는 '-'를 넣어 등식을 만들며 놀고 있다. 예를 들어, "8 3 2 4 8 7 2 4 0 8 8"에서 등식 "8+3-2-4+8-7-2-4-0+8=8"을 만들 수 있다.

상근이는 올바른 등식을 만들려고 한다. 상근이는 아직 학교에서 음수를 배우지 않았고, 20을 넘는 수는 모른다. 따라서, 왼쪽부터 계산할 때, 중간에 나오는 수가 모두 0 이상 20 이하이어야 한다. 예를 들어, "8+3+2-4-8-7+2+4+0+8=8"은 올바른 등식이지만, 8+3+2-4-8-7이 음수이기 때문에, 상근이가 만들 수 없는 등식이다.

숫자가 주어졌을 때, 상근이가 만들 수 있는 올바른 등식의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N이 주어진다. (3 ≤ N ≤ 100) 둘째 줄에는 0 이상 9 이하의 정수 N개가 공백으로 구분해 주어진다.

출력
첫째 줄에 상근이가 만들 수 있는 올바른 등식의 개수를 출력한다. 이 값은 263-1 이하이다.
'''


import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums, answer = nums[:-1], nums[-1]
MAX = 20
dp = [[0 for _ in range(MAX+1)] for _ in range(len(nums))]
# initialization
dp[0][nums[0]] = 1
for i in range(1, len(nums)):
    for j in range(MAX+1):
        if not dp[i-1][j]: continue
        if j + nums[i] <= MAX:
            dp[i][j+nums[i]] += dp[i-1][j]
        if j - nums[i] >= 0:
            dp[i][j-nums[i]] += dp[i-1][j]
print(dp[-1][answer])
