def count_one_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def solution(n):
    count = count_one_bits(n)
    next_number = n + 1
    while True:
        if count_one_bits(next_number) == count:
            return next_number
        next_number += 1

print(solution(78))
print(solution(15))