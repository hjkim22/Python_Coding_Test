def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced_array = array[i-1:j]
        sorted_sliced_array = sorted(sliced_array)
        answer.append(sorted_sliced_array[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))