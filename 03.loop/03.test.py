# p125.'주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고가라'
pocket = ['money','card','mobilephone']
if 'card' not in pocket:
    print("걸어가라")
else:
    print("버스를 타고가라")

# p136. 1부터 10까지 숫자중 3의 배수를 뺀 나머지 값을 출력
a = 0
while a < 10:
    a += 1
    if a % 3 == 0: continue
    print(a)

# p.142 for문 range 함수 사용, 1부터 100까지 더하기
add = 0
for i in range(1,101):
    add += i

print(add)

#Q2
result = 0
i = 1
while i <= 1000:
    if i%3 == 0:
        result += i
    i+=1

print(result)

#Q3
i = 0
while True:
    i+= 1
    if i>5: break
    print('*' * i)

#Q4
for i in range(1,101):
    print(i)

#Q5
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
    average = total/10 #또는 total/len(A)
    print(average)

#Q6
numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n%2==1]



