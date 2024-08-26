(num_of_taker, 
 math_passer, 
 english_passer, 
 math_english_passer) = map(int, input().split())

pass_list = [False for _ in range(num_of_taker)]

math_points = list(map(int, input().split()))
english_points = list(map(int, input().split()))
sum_points = [m + e for m, e in zip(math_points, english_points)]

sorted_math_points = sorted(math_points, reverse=True)
sorted_english_points = sorted(english_points, reverse=True)
sorted_sum_points = sorted(sum_points, reverse=True)

for num in sorted_math_points:
    if math_passer == 0:
        break

    index = math_points.index(num)
    if pass_list[index] == False:
        pass_list[index] = True
        math_passer -= 1
    
    math_points[index] = -1

for num in sorted_english_points:
    if english_passer == 0:
        break

    index = english_points.index(num)
    if pass_list[index] == False:
        pass_list[index] = True
        english_passer -= 1
    
    english_points[index] = -1

for num in sorted_sum_points:
    if math_english_passer == 0:
        break

    index = sum_points.index(num)
    if pass_list[index] == False:
        pass_list[index] = True
        math_english_passer -= 1

    sum_points[index] = -1

for i in range(num_of_taker):
    if pass_list[i]:
        print(i+1)