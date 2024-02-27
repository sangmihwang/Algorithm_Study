import sys
input = sys.stdin.readline

# def prime_list(n):
#     nums = [True]*n  # 일단 모두 소수(True)로 표시
#     m = int(n ** 0.5)
#     for i in range(2, m+1):
#         if nums[i] == True:
#             for j in range(i+i, n, i):
#                 nums[j] = False
#     return [i for i in range(2, n) if nums[i] == True]

M, N = map(int, input().split())

# primeN = prime_list(N)
# primeM = prime_list(M)
# ans = [x for x in primeN if x not in primeM]
# print(ans)

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)
        