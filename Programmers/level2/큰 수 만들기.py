def solution(number, k):

    st = [number[0]]
    for n in number[1:]:
        while st and st[-1] < n and k > 0:
            k -= 1
            st.pop()
        st.append(n)
    # print(st)
    if k != 0:
        st = st[:-k]
    return ''.join(st)