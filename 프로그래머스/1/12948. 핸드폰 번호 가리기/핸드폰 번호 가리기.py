def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]

phone_numbers = ["01033334444", "027778888"]

for phone_number in phone_numbers:
    print(solution(phone_number))