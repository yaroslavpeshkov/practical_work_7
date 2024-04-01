numbers = []
count = 0
for i in range(100, 999+1):
    if i % 17 == 0:
        numbers.append(str(i))
        count += 1
print(' '.join(numbers))
print(count)
