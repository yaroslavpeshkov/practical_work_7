import ru_local as ru

number_x = int(input(ru.INPUT_NUMBER))
summary = 0
for i in range(0, number_x+1):
    summary += i
print(summary)
