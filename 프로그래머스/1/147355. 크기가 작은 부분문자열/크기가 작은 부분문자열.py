def solution(t, p):
    def str_to_num(s):
        return int(s)

    count = 0
    p_value = str_to_num(p)
    for i in range(len(t) - len(p) + 1):
        sub_str = t[i:i+len(p)]
        sub_value = str_to_num(sub_str)
        if sub_value <= p_value:
            count += 1

    return count

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))