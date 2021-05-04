import math
def solution(nums):
    answer = 0
    total_num = len(nums) # N
    choose_num = math.floor(total_num / 2) # N/2
    if len(set(nums)) >= choose_num:
        answer = choose_num
    else:
        answer = len(set(nums))
    return answer
