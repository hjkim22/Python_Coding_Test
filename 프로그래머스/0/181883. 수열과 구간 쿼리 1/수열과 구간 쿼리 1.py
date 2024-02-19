def solution(arr, queries):
    for query in queries:
        for i in range(query[0], query[1] + 1):
            arr[i] += 1
    return arr

print(solution([0, 1, 2, 3, 4], [[0, 1],[1, 2],[2, 3]]))