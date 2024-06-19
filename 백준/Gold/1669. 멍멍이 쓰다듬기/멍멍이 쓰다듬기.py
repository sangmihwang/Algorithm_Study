import sys
input = sys.stdin.readline

monkey, dog = map(int, input().split())
d = dog - monkey
if d == 0:
    print(0)
elif d == 1:
    print(1)
elif d == 2:
    print(2)
else:
    for i in range(2, 2**16):
        if (i-1)**2 < d <= ((i-1)**2 + i**2)//2:
            print(2*i-2)
            break
        elif ((i-1)**2 + i**2)//2 < d <= i**2:
            print(2*i-1)
            break