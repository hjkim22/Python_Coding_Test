def solution(keyinput, board):
    x, y = 0, 0

    for direction in keyinput:
        if direction == "up" and y < (board[1] - 1) // 2:
            y += 1
        elif direction == "down" and y > -(board[1] - 1) // 2:
            y -= 1
        elif direction == "left" and x > -(board[0] - 1) // 2:
            x -= 1
        elif direction == "right" and x < (board[0] - 1) // 2:
            x += 1

    return [x, y]

print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))