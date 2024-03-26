people = []
result = 0

# a와 b의 입력은 4번씩(4개역을 지나니까)
# a는 내린 사람의 수, b는 탄 사람의 수 
for i in range(4):
    a, b = map(int, input().split())
    
    result = result - a + b
    people.append(result)
        
print(max(people))