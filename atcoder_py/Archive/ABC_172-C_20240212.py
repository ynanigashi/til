#TLE
num_of_books_a, num_of_books_b, time_limit = map(int, input().split())
time_of_books_a = list(map(int, input().split()))
time_of_books_a.insert(0, 0)
time_of_books_b = list(map(int, input().split()))
max_books = 0
sum_of_time_a = 0
for i, time_a in enumerate(time_of_books_a):
    sum_of_time_a += time_a
    sum_of_time = sum_of_time_a
    if sum_of_time > time_limit:
        break
    else:
        read_books = i
    for time_b in time_of_books_b:
        sum_of_time += time_b
        if sum_of_time > time_limit:
            break  
        read_books += 1
    max_books = max(max_books, read_books)
    
print(max_books)