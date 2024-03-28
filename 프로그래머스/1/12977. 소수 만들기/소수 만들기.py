def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    from itertools import combinations
    count = 0
    for combination in combinations(nums, 3):
        if is_prime(sum(combination)):
            count += 1
    return count

print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))