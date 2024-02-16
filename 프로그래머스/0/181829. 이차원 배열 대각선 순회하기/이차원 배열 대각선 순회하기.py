def solution(board, k):
    total_sum = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i + j <= k:
                total_sum += board[i][j]
    return total_sum

print(solution([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]], 2))