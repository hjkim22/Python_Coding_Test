def solution(n, left, right):
    result = []
    for i in range(left, right + 1):
        row = i // n
        col = i % n
        result.append(max(row, col) + 1)
    return result

print(solution(3, 2, 5))
print(solution(4, 7, 14))