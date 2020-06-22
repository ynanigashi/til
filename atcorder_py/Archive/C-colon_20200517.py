import math
A, B, H, M = map(int, input().split())
tan_kaku = H * 30 + M * 0.5
cho_kaku = M * 6
tan_x = math.cos(math.radians(tan_kaku)) * A
tan_y = math.sin(math.radians(tan_kaku)) * A
cho_x = math.cos(math.radians(cho_kaku)) * B
cho_y = math.sin(math.radians(cho_kaku)) * B
print(math.sqrt((tan_x - cho_x)**2 + (tan_y - cho_y)**2))