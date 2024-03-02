def solution(l, r):
    result = []
    for num in range(l, r + 1):
        if all(digit in ['0', '5'] for digit in str(num)):
            result.append(num)
    if not result:
        result = [-1]
    return result

print(solution(5, 555))
print(solution(10, 20))