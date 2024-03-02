def solution(picture, k):
    result = []
    for row in picture:
        expanded_row = ''.join([pixel * k for pixel in row])
        result.extend([expanded_row] * k)
    return result

print(solution([".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."], 2))
print(solution(["x.x", ".x.", "x.x"], 3))