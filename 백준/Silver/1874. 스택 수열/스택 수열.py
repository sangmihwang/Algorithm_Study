n = int(input())
lst = list(int(input()) for _ in range(n))
stack = []
ans = []
tmp = 1
for l in lst:
    while tmp <= l:
        stack.append(tmp)
        ans.append('+')
        tmp += 1
    if stack[-1] == l:
        stack.pop()
        ans.append('-')
if stack:
    print('NO')
else:
    print(*ans, sep='\n')