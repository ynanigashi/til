height, width = map(int, input().split())
num_of_rows, num_of_columns = map(int, input().split())
print((height - num_of_rows) * (width - num_of_columns))