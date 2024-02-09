def solution(array):
    count_dict = {}
    
    for num in array:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    max_count = max(count_dict.values())
    frequent_values = [key for key, value in count_dict.items() if value == max_count]
    
    if len(frequent_values) > 1:
        return -1
    else:
        return frequent_values[0]

print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))