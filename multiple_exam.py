from collections import OrderedDict

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = "happiness" #암호키
plain = "you look happy"
print(key)
#암호키 중복 제거 후 배열에 넣기
result = "".join(OrderedDict.fromkeys(key))
list = []
for i in result:
    list.append(i)

print(list)

# z입력하면 q로 바꾸어 처리하기
zCheck = []
for i in range(len(list)):
    if list[i] == 'z':
        list[i] = 'q'
        zCheck.append(i)

print(list)


# 암호판 만들기
for i in range(len(a)):
    if a[i] in list:
        continue
    else:
        list.append(a[i])
print(a)
print(list) #암호판

#2차원 배열 암호판 만들기
list2 = [[0 for col in range(5)] for row in range(5)]
cnt = 0
for i in range(len(list2)):
    for j in range(len(list2[i])):
        list2[i][j] = list[cnt]
        cnt += 1

print(list2) # 2차원 배열 암호판

# 평문 공백 제거
plain = plain.replace(" ", "")
print(plain)

# x가 필요한 위치에 x 넣기
list3 = []
flag = 1

list3.append(plain[0])
for i in range(1, len(plain)):
    if plain[i-1] != plain[i]:
        list3.append(plain[i])
    elif plain[i-1] == plain[i] and i % 2 == flag:
        list3.append('x')
        list3.append(plain[i])
        flag = (1 + flag) % 2
    else:
        list3.append(plain[i])
if len(list3) % 2 == 1:
    list3.append('x')

print(list3)

str = ''.join(list3)
print(str)


#문자열 두칸씩 나누기
list4 = []
for i in range(0, len(str), 2):
    list4.append(str[i:i+2])
str2 = " ".join(list4)
print(str2)


# list - 암호판
# list2 - 2차원 암호판
# list3 - x 자리에 넣기
# list4 - 두 글자씩 나누기

x1 = 0
x2 = 0
y1 = 0
y2 = 0
encArr = []
encResult = ""

for i in range(len(list4)):
    temp = [0, 0]

    for j in range(len(list2)):
        for k in range(len(list2[j])):
            if list2[j][k] == list4[i][0]:
                x1 = j
                y1 = k
            if list2[j][k] == list4[i][1]:
                x2 = j
                y2 = k

    #행이 같은 경우
    if x1 == x2:
        temp[0] = list2[x1][(y1+1)%5]
        temp[1] = list2[x2][(y2+1)%5]
    #열이 같은 경으
    elif y1 == y2:
        temp[0] = list2[(x1+1)%5][y1]
        temp[1] = list2[(x1+1)%5][y2]
    # 행과 열이 모두 다른 경우
    else:
        temp[0] = list2[x2][y1]
        temp[1] = list2[x1][y2]

    encArr.append(temp)

for i in range(len(encArr)):
    encResult += encArr[i][0] + encArr[i][1] + " "
print(encResult)

#복호화
arr = []
decArr = []

x1 = 0
x2 = 0
y1 = 0
y2 = 0

decResult = ""


encResult_blank = encResult.replace(" ", '')
print(encResult_blank)
for i in range(len(encResult_blank)):
    arr.append(encResult_blank[i])

print(arr)

for i in range(len(arr)):
    temp = [0, 0]

    for j in range(len(list2)):
        for k in range(len(list2[j])):
            if list2[j][k] == arr[i][0]:
                x1 = j
                y1 = k
            if list2[j][k] == arr[i][1]:
                x2 = j
                y2 = k

    #행이 같은 경우
    if x1 == x2:
        temp[0] = list2[x1][(y1+4)%5]
        temp[1] = list2[x2][(y2+4)%5]
    #열이 같은 경으
    elif y1 == y2:
        temp[0] = list2[(x1+4)%5][y1]
        temp[1] = list2[(x1+4)%5][y2]
    # 행과 열이 모두 다른 경우
    else:
        temp[0] = list2[x2][y1]
        temp[1] = list2[x1][y2]

    decArr.append(temp)

# print(decArr)

for i in range(len(decArr)):
    if i != len(decArr)-1 and decArr[i][1] == 'x' and decArr[i][0] == decArr[i + 1][0]:
        decResult += decArr[i][0]
    elif i == len(decArr)-1 and decArr[i][1] == 'x':
        decResult += decArr[i][0]
    else:
        decResult += decArr[i][0]+decArr[i][1]

if len(zCheck) != 0:
    for i in range(len(zCheck)):
        for j in range(len(decResult)):
            if zCheck[i] == j:
                decResult[j] = 'q'

print(decResult)