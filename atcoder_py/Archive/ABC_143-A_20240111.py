window_width, curtain_width = map(int, input().split())
print(max(0, window_width - curtain_width * 2))