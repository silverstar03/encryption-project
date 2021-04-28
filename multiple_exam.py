from collections import OrderedDict

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = "sleepy" #암호키
plain = "Are you sleepy"

#암호키 중복 제거 후 배열에 넣기
result = "".join(OrderedDict.fromkeys(key))
list = []
for i in result:
    list.append(i)

last = a.index(list[-1])  # 제일 마지막에 들어오는 알파벳 인덱스 가져오기

list2 = [[0 for col in range(5)] for row in range(5)]
for i in range(len(list2)):
    for j in range(len(list2[i])):
        cnt = 0
        list2[i][j] = result[cnt]
        cnt += 1
