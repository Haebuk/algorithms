def solution(brown, yellow):
    width, height = 0, 0
    line = 1
    
    while True:
        if 2 * line + 2 * (yellow + 2) == brown:
            width = yellow + 2
            height = line + 2
            break
        yellow /= 2
        line *= 2
        return [width, height]