P, K = map(int, input().split())

# BAD 케이스인 경우, 두 소수 중 작은 소수의 초깃값
badnum = K

for i in range(2,K) :
  if P % i == 0 :          # BAD 케이스인 경우
    if badnum > i :
      badnum = i           # 두 소수 중 작은 값 리턴 

if badnum != K :           # 초기값이 변경되었으므로 BAD 케이스라는 것
  print('BAD', badnum)
else :
  print('GOOD')