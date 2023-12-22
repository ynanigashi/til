len_of_string, index_of_target = map(int, input().split())
string = input()
print(string[:index_of_target - 1] + string[index_of_target - 1].lower() + string[index_of_target:])