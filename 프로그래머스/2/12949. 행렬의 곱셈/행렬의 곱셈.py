def solution(arr1, arr2):
    row_len = len(arr1)
    col_len = len(arr2[0])
    result = [[0] * col_len for _ in range(row_len)]  # 결과 행렬 초기화

    for i in range(row_len):
        for j in range(col_len):
            for k in range(len(arr1[0])):
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))