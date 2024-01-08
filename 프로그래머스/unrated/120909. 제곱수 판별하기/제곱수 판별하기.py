def solution(n):
    sqrt = int(n ** 0.5)
    if sqrt ** 2 == n:
        return 1
    else:
        return 2
    
print(solution(144))
print(solution(976))