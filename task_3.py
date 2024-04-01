import ru_local as ru

number = int(input(ru.INPUT_NUMBER))
while number**0.5 % 1 != 0:
    print(ru.WRONG_NUMBER)
    number = int(input(ru.INPUT_ANOTHER))
print(ru.RIGHT_NUMBER)
