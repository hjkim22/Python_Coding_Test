def solution(n_str):
    idx = 0
    for i in range(len(n_str)):
        if n_str[i] != '0':
            idx = i
            break
    return n_str[idx:]

print(solution("0010"))
print(solution("854020"))
