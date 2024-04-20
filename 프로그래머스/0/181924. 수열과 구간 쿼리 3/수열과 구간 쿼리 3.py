def solution(arr, queries):
    for query in queries:
        i, j = query
        arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]

print(solution(arr, queries))