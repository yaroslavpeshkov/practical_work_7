number_n, number_k, number_r = map(int, input().split())
days = 0
while number_n < number_r:
    number_n *= 1 + number_k/100
    days += 1
    print(number_n)
print(days+1)
