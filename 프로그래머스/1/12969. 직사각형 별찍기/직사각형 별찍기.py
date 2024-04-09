def print_rectangle(n, m):
    for _ in range(m):
        print('*' * n)

n, m = map(int, input().split())

print_rectangle(n, m)
