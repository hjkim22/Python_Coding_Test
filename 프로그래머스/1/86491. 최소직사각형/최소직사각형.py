def solution(sizes):
    max_width = 0
    max_height = 0
    
    for size in sizes:
        width, height = size
        if width < height:
            width, height = height, width
        max_width = max(max_width, width)
        max_height = max(max_height, height)
    
    return max_width * max_height

sizes1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

print(solution(sizes1))
print(solution(sizes2))
print(solution(sizes3))