alice_start, alice_end, bob_start, bob_end = map(int, input().split())
max_start = max(alice_start, bob_start)
min_end = min(alice_end, bob_end)
print(max(0, min_end - max_start))