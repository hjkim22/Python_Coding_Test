def solution(arr):
    result = []
    for num in arr:
        if num >= 50 and num % 2 == 0:
            result.append(num // 2)
        elif num < 50 and num % 2 != 0:
            result.append(num * 2)
        else:
            result.append(num)
    return result

arr = [1, 2, 3, 100, 99, 98]
print(solution(arr))