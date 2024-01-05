def solution(numbers):
    answer = [i * 2 for i in numbers]
    return answer



num1 = [1, 2, 3, 4, 5]
num2 = [1, 2, 100, -99, 1, 2, 3]

print(solution(num1))
print(solution(num2))