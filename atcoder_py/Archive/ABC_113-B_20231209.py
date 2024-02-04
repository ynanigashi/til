num_of_points = int(input())
temperature, target = map(lambda x: int(x)*1000, 
                          input().split())
altitudes = list(map(int, input().split()))
diff_of_temperatures = [abs(temperature - t*6 - target)
                        for t in altitudes]
print(diff_of_temperatures.index(
    min(diff_of_temperatures)) + 1)