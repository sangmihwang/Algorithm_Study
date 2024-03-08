# import sys
# input = sys.stdin.readline

for _ in range(10000):
    sen = input()
    ans = 'yes'
    if sen == '.':
        break
    stack = []
    i = 0
    while i < len(sen):
        if sen[i] == '(' or sen[i] == '[':
            stack.append(sen[i])
        elif sen[i] == ')':
            if stack:
                x = stack.pop()
                if x == '(':
                    pass
                else:
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
        elif sen[i] == ']':
            if stack:
                x = stack.pop()
                if x == '[':
                    pass
                else:
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
        i += 1
    if stack:
        ans = 'no'
    print(ans)