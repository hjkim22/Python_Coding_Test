def calculate(expression):
    x, op, y, eq, z = expression.split()
    x, y, z = int(x), int(y), int(z)
    if op == '+':
        return x + y == z
    elif op == '-':
        return x - y == z

def solution(quiz):
    results = []
    for expression in quiz:
        if calculate(expression):
            results.append("O")
        else:
            results.append("X")
    return results

quiz1 = ["3 - 4 = -3", "5 + 6 = 11"]
print(solution(quiz1))

quiz2 = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
print(solution(quiz2))