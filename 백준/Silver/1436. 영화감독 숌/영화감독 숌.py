## 백준_ 1436_ 영화감독 숌

N = int(input())

def sol():
    ans = []
    for i in range(10):
        for j in range(10):
            for h in range(10):
                for k in range(10):
                    num1 = str(i) + str(j) + str(h) + str(k) + '666'
                    num2 = str(i) + str(j) + str(h) + '666' + str(k)
                    num3 = str(i) + str(j) + '666' + str(h) + str(k)
                    num4 = str(i) + '666' + str(j) + str(h) + str(k)
                    num5 = '666' + str(i) + str(j) + str(h) + str(k)
                
                    ans += [int(num1), int(num2), int(num3), int(num4), int(num5)]
    ans = list(set(ans))
    ans.sort()
    
    return ans

print(sol()[N-1])