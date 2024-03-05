weather_str = input()
if weather_str == 'RRR':
    print(3)
elif weather_str == 'RSR':
    print(1)
elif weather_str.count('R') == 2:
    print(2)
elif 'R' in weather_str:
    print(1)
else:
    print(0)