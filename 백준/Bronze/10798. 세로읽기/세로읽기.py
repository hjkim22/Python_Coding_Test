words = [input() for _ in range(5)]

result = ''
max_len = max(len(word) for word in words)

for i in range(max_len):
    for word in words:
        if i < len(word):
            result += word[i]

print(result)