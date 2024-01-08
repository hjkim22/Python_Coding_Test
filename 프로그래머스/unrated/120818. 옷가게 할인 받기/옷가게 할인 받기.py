def solution(price):
    discount_rate = 0
    if price >= 500000:
        discount_rate = 0.2
    elif price >= 300000:
        discount_rate = 0.1
    elif price >= 100000:
        discount_rate = 0.05
        
    discount = price * discount_rate
    result = price - discount
    return int(result)

print(solution(150000))
print(solution(580000))