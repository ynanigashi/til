num_of_items, num_of_buy = map(int, input().split())
votes = list(map(int, input().split()))
total_votes = sum(votes)
min_votes = total_votes / (4 * num_of_buy)
can_buy = 0
for vote in votes:
    if vote >= min_votes:
        can_buy += 1

print('Yes' if can_buy >= num_of_buy else 'No')