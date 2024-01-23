def solution(n):
    i = 1
    factorial = 1
    
    while factorial <= n:
        i += 1
        factorial *= i
    
    return i - 1

print(solution(3628800))
print(solution(7))