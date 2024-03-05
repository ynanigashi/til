num_of_words = int(input())
words = set()
ex_words = set()

for _ in range(num_of_words):
    word = input()
    if word[0] == '!':
        ex_words.add(word[1:])
    else:
        words.add(word)

unsatisfiable_words = words & ex_words

print('satisfiable' 
      if len(unsatisfiable_words) == 0 
      else unsatisfiable_words.pop())