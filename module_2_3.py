my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
numbers = 0
while len(my_list) > numbers:
    print(my_list[numbers])
    numbers = numbers + 1
    if my_list[numbers] >= 0:
        continue
    if my_list[numbers] < 0:
        break




