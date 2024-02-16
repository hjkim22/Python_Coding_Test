def solution(n):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer

print(solution(3))
print(solution(6))
print(solution(1))