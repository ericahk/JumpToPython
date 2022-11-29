# 1.평균점수 연산
a=80
b=75
c=55
avg=(a+b+c)/3
print(avg)

# 2.자연수 13 홀/짝 판별 방법
if (13%2) == 0:
    print("짝수")
else:
    print("홀수")

# 3.주민번호 881120-1068234 슬라이싱 출력 테스트
pin = "881120-1068234"
yyyymmdd = pin[:6] #슬라이싱 두번째는 -1까지로 끊으므로.
num = pin[7:]
print(yyyymmdd)
print(num)

# 4.주민등록번호에서 성별을 나타내는 숫자 출력
pin = "881120-1068234"
print(pin[7])

# 5.문자열 replace 함수 사용 #치환 출력
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

# 6.리스트 정렬 순서 변경
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# 7.리스트로 문자열 만들기
a = ['Life','is','too','sort']
result = " ".join(a)
print(result)

# 8.튜플에 값 추가
a = (1,2,3)
a = a + (4,) #튜플은 요솟값 하나일때 뒤에 콤마넣어야함
print(a)

# 10.딕셔너리에서 값 추출
a = {'A':90,'B':80,'C':70}
result = a.pop('B')
print(a)
print(result)

# 11.리스트에서 중복 숫자 제거
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a) #리스트를 집합으로 변환(중복값 허용 안함)
b = list(aSet) #집합을 다시 리스트로 변환
print(b)
