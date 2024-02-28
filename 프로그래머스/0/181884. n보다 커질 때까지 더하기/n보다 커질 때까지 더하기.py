def solution(numbers, n):
    total = 0
    for num in numbers:
        total += num
        if total > n:
            break
    return total

print(solution([34, 5, 71, 29, 100, 34], 123))
print(solution([58, 44, 27, 10, 100], 139))
