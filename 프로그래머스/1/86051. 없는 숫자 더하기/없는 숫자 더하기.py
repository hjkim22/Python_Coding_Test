def solution(numbers):
    total = 45
    for num in numbers:
        total -= num
    return total

numbers1 = [1, 2, 3, 4, 6, 7, 8, 0]
numbers2 = [5, 8, 4, 0, 6, 7, 9]
print(solution(numbers1))
print(solution(numbers2))