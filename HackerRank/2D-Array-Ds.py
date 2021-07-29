def hourglassSum(arr):
    max_hourglass = -9 * 7
    for i in range(4):
        for j in range(4):
            hourglass = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            max_hourglass = hourglass if hourglass > max_hourglass else max_hourglass
    return max_hourglass
