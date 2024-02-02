def solution(dots):
    width = max(dots[0][0], dots[1][0], dots[2][0], dots[3][0]) - min(dots[0][0], dots[1][0], dots[2][0], dots[3][0])
    
    height = max(dots[0][1], dots[1][1], dots[2][1], dots[3][1]) - min(dots[0][1], dots[1][1], dots[2][1], dots[3][1])
    
    area = width * height
    
    return area

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))