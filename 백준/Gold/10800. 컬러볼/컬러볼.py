import sys
input = sys.stdin.readline

N = int(input())
balls = []
for i in range(N):
    C, S = map(int, input().split())
    balls.append((C, S, i))

balls.sort(key=lambda x: x[1])
results = [0] * N

# 색상별 합과 전체 합을 계산
color_sum = {}
total_sum = 0
j = 0  # 이전에 살펴본 위치

# 각 공들을 차례로 보면서
for i in range(N):
    while balls[j][1] < balls[i][1]:
        color = balls[j][0]
        size = balls[j][1]
        if color in color_sum:
            color_sum[color] += size
        else:
            color_sum[color] = size
        total_sum += size
        j += 1
    
    tmpC = balls[i][0]
    tmpS = balls[i][1]
    tmpI = balls[i][2]

    results[tmpI] = total_sum - color_sum.get(tmpC, 0)

# 결과 출력
for result in results:
    print(result)
