def solution(n):
    divisors_sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

print(solution(12))
print(solution(5))