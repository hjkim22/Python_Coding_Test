from itertools import combinations

def solution(number):
    count = 0
    for combo in combinations(number, 3):
        if sum(combo) == 0:
            count += 1
    return count

number1 = [-2, 3, 0, 2, -5]
number2 = [-3, -2, -1, 0, 1, 2, 3]
number3 = [-1, 1, -1, 1]

print(solution(number1))
print(solution(number2))
print(solution(number3))