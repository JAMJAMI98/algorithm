import datetime as dt

# 입력 받아서 날짜 및 시간 객체로 변환
now = dt.datetime.strptime(input(), '%B %d, %Y %H:%M')

# 해당 연도의 첫 번째 날과 마지막 날 구하기
year_start = dt.datetime(now.year, 1, 1)
next_year_start = dt.datetime(now.year +1, 1, 1)

# 연도의 총 일수와 현재 날짜가 연도의 첫날로부터 몇 일째인지 계산하기
total_seconds = (next_year_start - year_start).total_seconds()
today_seconds = (now - year_start).total_seconds()

# 퍼센트로 나타내기
percent = (today_seconds / total_seconds) * 100

# 소수점 열 다섯째 자리까지 출력
print(f'{percent:.15f}%')