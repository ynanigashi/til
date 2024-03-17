str = input()
print('Yes' if str[0] == '<' 
      and str[-1] == '>' 
      and len(set(str[1:-1])) == 1
      and str[1] == '='
      else 'No'
      )