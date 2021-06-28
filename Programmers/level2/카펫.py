def solution(brown, yellow):

    for height in range(1, int(yellow/2)+1):
        if yellow % height != 0: # height가 yellow의 약수가 아닌 경우
            continue
            
        else: # 약수인 경우
            width = yellow / height
            
        if (width + 2) * 2 + (height * 2) == brown:
            return [width+2, height+2]
        
    return [3,3] # yellow가 1인 경우