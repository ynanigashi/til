old, target, stop, tall, growth = map(int, input().split())
print(tall - max(stop - target, 0)*growth)