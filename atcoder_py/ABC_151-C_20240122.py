num_of_questions, num_of_answers = map(int, input().split())
answers = [input().split() for _ in range(num_of_answers)]
ac_cnt = 0
wa_cnt = 0
ac_set = set()
for answer in answers:
    if answer[0] not in ac_set:
        if answer[1] == 'AC':
            ac_cnt += 1
            ac_set.add(answer[0])
        else:
            wa_cnt += 1

print(ac_cnt, wa_cnt)