temperature = float(input())
count = 0
while temperature != 0:
    temperature_1 = temperature
    temperature = float(input())
    if temperature_1 > temperature:
        count += 1
print(count-1)
