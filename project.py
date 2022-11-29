def solution(string):
    st = []
    for i in string:
        if i != '*':
            st.append(i)
        else:
            if st != []:
                st = st[:-1]
    if st == []:
        return ''
    return ''.join(st)






