N, M = map(int, input().split())
if N > M:
    N, M = M, N     # N < M로 정렬
def div(n):
    ans = {}
    if n <= 2:
        ans[n] = 1
        return ans
    for i in range(2, n+1):
        while True:
            if n % i == 0:
                ans[i] = ans.get(i, 0) + 1
                n = n // i
            else:
                break
    return ans

ansN = div(N)
ansM = div(M)
# print(ansM, ansN)
minV = 1       # 최소공배수
maxV = 1       # 최대공약수

for i in range(2, M+1):
    if i in ansN and i in ansM:
        maxV = maxV*(i**min(ansN[i], ansM[i]))
        minV = minV*(i**max(ansN[i], ansM[i]))
    elif i in ansN and i not in ansM:
        minV = minV*(i**ansN[i])
    elif i not in ansN and i in ansM:
        minV = minV*(i**ansM[i])
print(maxV)
print(minV)
     
