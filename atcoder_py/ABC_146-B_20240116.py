def char_to_num(char):
    return ord(char) - 65

def num_to_char(num):
    return chr(num + 65)

index_of_char = int(input())
str = input()
for c in str:
    print(num_to_char((char_to_num(c) + index_of_char) % 26), end='')