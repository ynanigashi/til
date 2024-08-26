minuites = int(input())
h, m = divmod(minuites, 60)
print(f'{21+h}:{str(m).zfill(2)}')