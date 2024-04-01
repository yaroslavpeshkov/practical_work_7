string = input()
input_list = list(string)
input_length = len(input_list)
output_list = []
for i in range(0, input_length):
    if (i+1) % 3 == 0:
        output_list.append(input_list[i])
print(''.join(output_list))
