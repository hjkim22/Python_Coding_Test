def solution(n):
    result = 0
    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result += 1
            pair = n // i
            if i != pair:
                result += 1
    return result
        
print(solution(20))
print(solution(100))