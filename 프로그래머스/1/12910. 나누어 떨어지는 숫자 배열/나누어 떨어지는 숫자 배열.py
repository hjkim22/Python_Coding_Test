def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    answer.sort()
    if not answer:
        answer.append(-1)
    return answer

arr1 = [5, 9, 7, 10]
divisor1 = 5
print(solution(arr1, divisor1))

arr2 = [2, 36, 1, 3]
divisor2 = 1
print(solution(arr2, divisor2))

arr3 = [3, 2, 6]
divisor3 = 10
print(solution(arr3, divisor3))