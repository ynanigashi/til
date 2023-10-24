A_width, A_height, B_width, B_height = map(int, input().split())
A_area, B_area = A_width*A_height, B_width*B_height
print(max(A_area, B_area))