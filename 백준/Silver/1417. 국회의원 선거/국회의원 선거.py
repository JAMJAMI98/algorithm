n = int(input())
vote = [int(input()) for _ in range(n)]

# 다솜이의 처음 득표 수
dasom = vote[0]

# 다른 후보자의 득표 수
other_vote = vote[1:]

# 매수 인원
people = 0

# 가장 높은 득표 수 보기위한 내림차순 정렬
other_vote.sort(reverse=True)

while other_vote and dasom <= other_vote[0]:
  other_vote[0] -= 1
  dasom += 1
  people += 1

  other_vote.sort(reverse=True)

print(people)