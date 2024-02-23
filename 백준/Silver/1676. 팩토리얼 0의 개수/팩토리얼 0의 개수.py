N = int(input())

fac = 1
for n in range(1, N+1):
    fac = fac*n
cnt = 0
facS = str(fac)

for i in range(len(facS)-1, -1, -1):
    if facS[i] == '0':
        cnt += 1
    else:
        break
print(cnt)