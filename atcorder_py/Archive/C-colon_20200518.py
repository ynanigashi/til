import math
A, B, H, M = map(int, input().split())
tan_kaku = H * 30 + M * 0.5
cho_kaku = M * 6
rad = math.radians(abs(tan_kaku-cho_kaku))
print(math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(rad)))