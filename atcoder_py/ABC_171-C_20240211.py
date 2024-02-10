def generate_dogs_name(dogs_num):
    dogs_name = ''
    while dogs_num > 0:
        dogs_num -= 1
        dogs_name = chr(97 + dogs_num % 26) + dogs_name
        dogs_num = dogs_num // 26
    return dogs_name

print(generate_dogs_name(int(input())))