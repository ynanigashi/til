steps = input()
even_steps = steps[::2]
odd_steps = steps[1::2]
print('Yes' 
      if 'L' not in even_steps and 
         'R' not in odd_steps 
         else 'No')