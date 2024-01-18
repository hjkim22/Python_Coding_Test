def solution(n):
    def is_composite(num):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count >= 3

    return sum(1 for num in range(4, n + 1) if is_composite(num))

print(solution(10))
print(solution(15))