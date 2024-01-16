def solution(cipher, code):
    answer = ""
    code -= 1

    for i in range(code, len(cipher), code + 1):
        answer += cipher[i]

    return answer


print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))