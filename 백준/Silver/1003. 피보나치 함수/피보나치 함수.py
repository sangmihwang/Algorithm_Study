T = int(input())
# fibo = [0]*40
# fibo[0], fibo[1] = 1, 1
# for i in range(2, 40):
#     fibo[i] = fibo[i-1]+fibo[i-2]
# print(fibo)

    # cnt0 = 0
    # cnt1 = 0
    # fib(N)
    # print(cnt0, cnt1)
lst = [[0, 0]]*41
lst[0] = [1, 0]
lst[1] = [0, 1]
# print(lst)
for i in range(2, 41):
    lst[i] = [lst[i-1][0] + lst[i-2][0], lst[i-1][1] + lst[i-2][1]]
for _ in range(T):
    N = int(input())
    print(lst[N][0], lst[N][1])