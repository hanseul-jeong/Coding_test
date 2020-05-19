

# 실패. -> [2, 20, 200] -> "220200" 이런 경우 때문
# def revalue(number_list):
#     flag = False
#     for k, v, th in number_list:
#         if th+1 != len(v):
#             flag = True
#     if flag and len(number_list)==1:
#         flag = False
#     return flag
# def cmp_numbers(number_list):   #(key value, origin value, th)
#     number_list.sort(reverse=True)
#     equal_cnt = 0
#     for idx in range(1, len(number_list)):
#         if number_list[idx][0] != number_list[0][0]:break
#         equal_cnt+=1
#     if equal_cnt+1 == len(number_list): # all of key value is equal
#         if revalue(number_list):        # compare next (th)
#                 for idx, (k, v, th) in enumerate(number_list):
#                     if th+1 != len(v):
#                         th += 1
#                         k = int(v[th])
#                         number_list[idx] = (k, v, th)
#                 return cmp_numbers(number_list)
#         else:   # all values of list is equal
#             return ''.join([v for k,v,th in number_list])
#     elif equal_cnt == 0:
#         return number_list[0][1] + cmp_numbers(number_list[1:])
#     else:
#         return cmp_numbers(number_list[:equal_cnt+1]) + cmp_numbers(number_list[equal_cnt+1:])
            
# def solution(numbers):
#     numbers = [str(v) for v in numbers]
#     candidates = sorted([(int(v[0]), v, 0) for v in numbers])
#     answer = cmp_numbers(candidates)
#     return str(int(answer))

