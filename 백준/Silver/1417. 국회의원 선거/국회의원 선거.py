import heapq

# 입력 처리
N = int(input().strip())
votes = [int(input().strip()) for _ in range(N)]

# 다솜이의 초기 득표 수
dasom_votes = votes[0]
# 다른 후보들의 득표 수 리스트 (최대 힙으로 사용)
other_votes = [-v for v in votes[1:]]  # 음수로 저장하여 최대 힙처럼 사용

# 힙 구성
heapq.heapify(other_votes)

# 매수한 사람의 수
bribes = 0

# 최대 힙에서 가장 큰 값을 가져와 다솜이의 득표 수와 비교
while other_votes and dasom_votes <= -other_votes[0]:
    # 가장 높은 득표수를 가진 후보에게서 1표 매수
    max_votes = -heapq.heappop(other_votes)  # 가장 높은 득표수
    max_votes -= 1  # 1표 매수
    dasom_votes += 1
    bribes += 1
    # 다시 힙에 삽입
    heapq.heappush(other_votes, -max_votes)

print(bribes)
