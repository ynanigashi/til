number = input()
without_post_zero = ''
post_flag = True
for c in number[::-1]:
    if c == '0' and post_flag:
        continue
    else:
        post_flag = False
    without_post_zero += c

print('Yes' if without_post_zero == without_post_zero[::-1] else 'No')