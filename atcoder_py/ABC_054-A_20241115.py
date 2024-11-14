alice, bob = map(int, input().split())
if alice == bob:
    print('Draw')
elif min(alice, bob) == 1:
    print('Alice' if alice == 1 else 'Bob')
else:
    print('Alice' if alice > bob else 'Bob')