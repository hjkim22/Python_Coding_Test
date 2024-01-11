def solution(n, k):
    kochi = n * 12000
    drink = k * 2000
    discount = (n // 10) * 2000
    price = kochi + drink - discount
    
    return price

print(solution(10, 3))
print(solution(64, 6))