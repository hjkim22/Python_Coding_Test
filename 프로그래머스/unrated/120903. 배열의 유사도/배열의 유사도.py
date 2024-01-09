def solution(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)
    
    return len(set_s1 & set_s2)


print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))