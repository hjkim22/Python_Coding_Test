def solution(array, height):
    order = 0
    
    for i in array:
        if i > height:
            order += 1
    return order

arr1 = [149, 180, 192, 170]
arr2 = [180, 120, 140]

print(solution(arr1, 167))
print(solution(arr2, 190))