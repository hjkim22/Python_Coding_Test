def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer

num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [89,90,91,92,93,94,95,96,97,98,99]

print(solution(num1))
print(solution(num2))