# 컵 위치를 바꾼 횟수
n = int(input())

cup = [1,2,3]

# n번 반복
for i in range(n) :
  x,y = map(int, input().split())

  x1 = cup.index(x)
  y1 = cup.index(y)

  cup[x1], cup[y1] = cup[y1], cup[x1]  # swap으로 컵 위치 바꾸기

# 공이 들어있는 컵번호 출력
print(cup[0])