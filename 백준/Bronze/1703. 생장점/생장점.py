while 1 :
  li = list(map(int, input().split()))
  
  # 처음 심는 것은 가지 하나에 잎이 하나 달린 묘목
  leaf = 1

  # 0이 입력되면 종료
  if li[0] == 0:
    break

  # 잎의 수 = 가지 수(splitting factor) * 생장점 - 가지치기
  else :
    for i in range(1, len(li), 2):
      leaf = leaf*li[i]-li[i+1]
    print(leaf)