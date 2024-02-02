n = int(input())
fizzbuzz_row = [i for i in range(n+1) 
                if not (i % 3 == 0 or i % 5 == 0)]
print(sum(fizzbuzz_row))