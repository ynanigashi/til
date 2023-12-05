string = input()
if string[0] == 'A' and string[2:-1].count('C') == 1:
    string = (string[1] 
              + string[2:-1].replace('C', '') 
              + string[-1])
    if string.islower():
        print('AC')
        exit()
print('WA')