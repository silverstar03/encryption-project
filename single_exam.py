from collections import OrderedDict
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = "passionate" #암호키
plain = "be careful for assassinator"

#암호키 중복 제거 후 배열에 넣기
result = "".join(OrderedDict.fromkeys(key))
list = []
for i in result:
    list.append(i)

last = a.index(list[-1]) #제일 마지막에 들어오는 알파벳 인덱스 가져오기

# 암호판 만들기
for i in range(last+1, len(a)):
    if a[i] in list:
        continue
    else:
        list.append(a[i])

for i in range(last):
    if a[i] in list:
        continue
    else:
        list.append(a[i])
print(a)
print(list) #암호판

list2 = []
# 평문 배열에 넣기
for i in plain:
   list2.append(i)

print(list2) #평문

# 암호문 들어가기
list3 = []
for i in list2:
    if i != ' ':
        num = a.index(i)
        list3.append(list[num])
    else:
        list3.append(i)

print(list3) #암호문

