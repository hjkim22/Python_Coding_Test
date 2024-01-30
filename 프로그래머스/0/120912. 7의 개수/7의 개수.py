def solution(array):
    return sum(str(x).count('7') for x in array)

array1 = [7, 77, 17]
array2 = [10, 29]

print(solution(array1))
print(solution(array2))