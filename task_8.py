number_n = int(input())
count = 0
while number_n > 0:
    number_n //= 2
    count += 1
print(count)
