n = int(input())
first_digit = n//100
last_digit = n%10
is_palindrome = first_digit == last_digit
print('Yes' if is_palindrome else 'No')