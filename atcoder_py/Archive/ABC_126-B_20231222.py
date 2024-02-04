target_string = input()
first_half = int(target_string[:2])
second_half = int(target_string[2:])
is_YYMM = True if 0 < second_half < 13 else False
is_MMYY = True if 0 < first_half < 13 else False
if is_YYMM and is_MMYY:
    print('AMBIGUOUS')
elif is_YYMM:
    print('YYMM')
elif is_MMYY:
    print('MMYY')
else:
    print('NA')