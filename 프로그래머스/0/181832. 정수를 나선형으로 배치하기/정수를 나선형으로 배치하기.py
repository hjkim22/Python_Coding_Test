def solution(n):
    result = [[0] * n for _ in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    num = 1
    x, y = 0, 0
    direction_idx = 0

    for _ in range(n*n):
        result[x][y] = num
        num += 1

        nx, ny = x + directions[direction_idx][0], y + directions[direction_idx][1]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or result[nx][ny] != 0:
            direction_idx = (direction_idx + 1) % 4
            nx, ny = x + directions[direction_idx][0], y + directions[direction_idx][1]

        x, y = nx, ny

    return result

print(solution(4))
print(solution(5))