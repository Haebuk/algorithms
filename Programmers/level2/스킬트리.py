def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees: # 유저가 만든 스킬트리별로 반복
        temp = 0 # 맞는 스킬 수 체크
        data ='' # 문자열 저장
        q = list(skill) # 스킬문자열을 리스트로 변환
        
        for a in st: # 각 알파벳
            if not q: # 리스트 비어있으면 탈출
                break
            if a in q: # 리스트에 스킬이 들어있으면
                q.remove(a) #리스트에서 해당 스킬 제거
                data += a # 문자열에 해당 스킬 추가

        for a in range(len(data)): # 문자열의 길이만큼 반복
            if data[a] != skill[a]: # 스킬순서가 다르면 종료
                break
            temp += 1 # 스킬순서가 같으면 +1
        
        if temp == len(data): # 스킬 순서가 전부 같으면 정답+1
            answer += 1
                
    return answer