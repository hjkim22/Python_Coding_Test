def solution(n, k):
    return [i for i in range(1, n + 1) if i % k == 0]

print(solution(10, 3))
print(solution(15, 5))