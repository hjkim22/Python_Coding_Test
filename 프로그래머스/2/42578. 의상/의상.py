def solution(clothes):
    from collections import defaultdict

    clothes_dict = defaultdict(int)
    for name, kind in clothes:
        clothes_dict[kind] += 1
    
    combinations = 1
    for count in clothes_dict.values():
        combinations *= (count + 1)
    
    return combinations - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) 
