import sys
input = sys.stdin.readline

N = int(input())
bag = 0

while N > 0:
    if N % 5 == 0:
        bag += N // 5
        break
    else:
        if N == 1 or N == 2:
            bag = -1
            break
        N -= 3
        bag += 1
print(bag)