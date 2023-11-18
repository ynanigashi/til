(
    num_of_cats, 
    num_of_cats_dogs, 
    num_of_exact_cats
    ) = map(int, input().split())

print('YES' 
      if num_of_cats <= num_of_exact_cats <= num_of_cats + num_of_cats_dogs 
      else 'NO'
      )
