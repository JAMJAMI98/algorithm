N, K = map(int, input().split())
medals = []

for _ in range(N):
    medals.append(list(map(int, input().split())))

# 등수 정렬
medals.sort(key = lambda x: (x[1], x[2], x[3]), reverse=True)

# 국가 인덱스 찾기
target_index = [medals[i][0] for i in range(N)].index(K)

# 등수찾기
for i in range(N):
    if medals[target_index][1:] == medals[i][1:]:
        print(i+1)
        break