def solution(rsp):
    result = ''
    for char in rsp:
        if char == '2':
            result += '0'
        elif char == '0':
            result += '5'
        elif char == '5':
            result += '2'
    return result

print(solution("2"))
print(solution("205"))