import sys
input = sys.stdin.readline

T = int(input())

for i in range(T) :
  temp = input()     # 빈 칸 입력 받기
  N = int(input())

  sum = 0
  for j in range(N) :
    sum += int(input())

  if sum % N ==  0 :
    print('YES')
  else :
    print('NO')