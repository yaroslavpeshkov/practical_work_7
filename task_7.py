import ru_local as ru

answer = int(input())
while answer % 1 == 0 and answer != 2:
    answer = answer / 2
if answer == 2:
    print(ru.CORRECT)
else:
    print(ru.NOT_CORRECT)
