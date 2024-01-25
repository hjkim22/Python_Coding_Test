def solution(numbers, direction):
    n = len(numbers)
    
    if direction == "right":
        rotated_numbers = [numbers[(i - 1) % n] for i in range(n)]
    elif direction == "left":
        rotated_numbers = [numbers[(i + 1) % n] for i in range(n)]
    
    return rotated_numbers

result1 = solution([1, 2, 3], "right")
print(result1)

result2 = solution([4, 455, 6, 4, -1, 45, 6], "left")
print(result2)