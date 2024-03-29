# math 모듈 import : 조합 mCn 계산을 위해서
import math

T = int(input())

for i in range(T) :
  n, m = map(int, input().split())
  bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
  print(bridge)