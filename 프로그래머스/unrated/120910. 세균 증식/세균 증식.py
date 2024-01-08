def solution(n, t):
    germ = n
    for i in range(t):
        germ *= 2
    return germ

print(solution(2, 10))
print(solution(7, 15))