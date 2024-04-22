n = int(input())

words = [str(input()) for i in range(n)]

# 중복제거
words = list(set(words))

# 오름차순 정렬
words.sort()

# 길이 기준으로 정렬
words.sort(key=len)

for i in words:
    print(i)