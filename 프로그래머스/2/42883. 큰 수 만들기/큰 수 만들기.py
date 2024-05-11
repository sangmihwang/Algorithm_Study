# def solution(number, k):
#     answer = ''
#     stack = []
#     cnt = 0
#     for i in range(len(number)):
#         if cnt == k:
#             stack += number[i:] 
#             break
#         if not stack:
#             stack.append(number[i])
#             continue
#         while stack:
#             if int(stack[-1]) < int(number[i]):
#                 stack.pop()
#                 cnt += 1
#                 if cnt == k:
#                     break
#             else:
#                 break
#         stack.append(number[i])         

#     answer = ''.join(stack)    
#     return answer



def solution(number, k):
    stack = []
    
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1

        stack.append(num)
        # print(stack)
        
    if k != 0:
        stack = stack[:-k]
    
    return ''.join(stack)