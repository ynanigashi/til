a, b = map(int,input().split())
rounded_num = round(b/a, 3)
formatted_num = "{:.3f}".format(rounded_num)
print(formatted_num)