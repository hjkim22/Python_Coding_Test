def solution(q, r, code):
    result = ""
    for i in range(len(code)):
        if i % q == r:
            result += code[i]
    return result

print(solution(3, 1, "qjnwezgrpirldywt"))
print(solution(1, 0, "programmers"))