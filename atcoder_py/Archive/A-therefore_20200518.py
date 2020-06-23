N = int(input()) % 10
if N in (2, 4, 5, 7, 9):
 print('hon')
elif str(N) in '0168':
 print('pon')
else:
 print('bon')