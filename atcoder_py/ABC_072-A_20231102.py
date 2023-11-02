sand_g, time_s = map(int, input().split())
remain_sand = sand_g - time_s
print( '0' if remain_sand <= 0 else remain_sand)