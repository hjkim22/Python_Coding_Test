def solution(n):
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False

    primes = [num for num in range(2, n + 1) if numbers[num]]
    
    return len(primes)

print(solution(10))
print(solution(5))