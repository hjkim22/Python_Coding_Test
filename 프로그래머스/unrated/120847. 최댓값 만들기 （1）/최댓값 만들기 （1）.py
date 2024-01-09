def solution(numbers):
    numbers.sort()
    
    max_num = numbers[-1] * numbers[-2]
    return max_num
                  
print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))                  