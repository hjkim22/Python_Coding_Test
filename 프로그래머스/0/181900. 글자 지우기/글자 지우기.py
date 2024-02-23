def solution(my_string, indices):
    result = ''
    for idx, char in enumerate(my_string):
        if idx not in indices:
            result += char
    return result

print(solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]))
