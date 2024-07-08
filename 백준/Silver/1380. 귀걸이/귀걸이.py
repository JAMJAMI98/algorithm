s = 0

while True:
  n = int(input())
  if n == 0:
    break

  # 여학생 이름
  name = [input().strip() for _ in range(n)]
  # 귀걸이를 압수당한 여학생 번호 추적 리스트
  cnt = []

  # 압수 및 반환 기록
  for _ in range(2 * n -1):
    a, b = input().split()
    if a not in cnt:
      cnt.append(a)
    else:
      cnt.remove(a)

  s += 1
  print(s, name[int(cnt[0]) - 1])