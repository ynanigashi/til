num_of_friends, having_money = map(int, input().split())
friends = [tuple(map(int, input().split())) for _ in range(num_of_friends)]
friends.sort(key=lambda x: x[0])
answer = 0
for village, money in friends:
      if having_money < village - answer:
            answer += having_money
            break
      else:
            having_money -= village - answer
            having_money += money
            answer = village

else:
      answer += having_money
print(answer)