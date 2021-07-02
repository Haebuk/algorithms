def solution(s):
    st = [s[0]]
    for a in s[1:]:
        # print(st)
        if not st:
            st.append(a)
        elif st[-1] == a:
            st.pop()
        else: 
            st.append(a)
        
    if st:
        return 0
    else:
        return 1
    return