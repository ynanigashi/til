n = int(input())
handreds_place = n // 100
print(handreds_place * 111 
      if n <= handreds_place * 111
      else (handreds_place + 1) * 111)