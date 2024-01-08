def solution(slice, n):
    pizza = (slice + n - 1) // slice
    return pizza

print(solution(7, 10))
print(solution(4, 12))