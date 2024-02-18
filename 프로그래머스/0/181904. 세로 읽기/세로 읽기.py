def solution(my_string, m, c):
    result = ''
    for i in range(c - 1, len(my_string), m):
        result += my_string[i]
    return result

print(solution("ihrhbakrfpndopljhygc", 4, 2))
print(solution("programmers", 1, 1))