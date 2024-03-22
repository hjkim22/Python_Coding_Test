def solution(arr1, arr2):
    answer = []
    row = len(arr1)
    col = len(arr1[0])

    for i in range(row):
        temp = []
        for j in range(col):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)

    return answer

arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]

print(solution(arr1, arr2))

arr3 = [[1], [2]]
arr4 = [[3], [4]]

print(solution(arr3, arr4))