def is_full_count(list1, list2):
    for i in range(len(list1)):
        if list1[i] == 'x' and list2[i] == 'x':
            return False
    return True

num_of_inputs, num_of_questions = map(int, input().split())
inputs = [input() for _ in range(num_of_inputs)]
cnt = 0
for i in range(num_of_inputs):
    for j in range(i + 1, num_of_inputs):
        if is_full_count(inputs[i], inputs[j]):
            cnt += 1

print(cnt)