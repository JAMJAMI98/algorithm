import sys
input = sys.stdin.readline

T = int(input())

for i in range(T) :
  a, b = map(int, input().split())

  if b % 4 == 0 :
    b = 4
  else :
    b = b % 4
    
  answer = a**b
  
  if answer % 10 == 0 :
    print(10)
  else :
    print(answer % 10)