def solution(arr, queries):
    result = []
    for query in queries:
        s, e, k = query
        sub_array = arr[s:e+1]
        sub_array = sorted(sub_array)
        answer = -1
        for num in sub_array:
            if num > k:
                answer = num
                break
        result.append(answer)
    return result

print(solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))