import sys
input = sys.stdin.readline

H, W = map(int, input().split())
rain = list(map(int, input().split()))
water = 0
for i in range(1, W-1):
    left = max(rain[:i])
    right = max(rain[i+1:])
    if min(left, right) > rain[i]:
        water += min(left, right)-rain[i]

print(water)