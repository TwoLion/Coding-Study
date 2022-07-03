# 반복문

# 특정한 소스코드를반복적으로 실행할 때 사용하는 문법
# while, for문, for문이 간결한 경우 많음
# R과는 달라서 조건을 걸 때 괄호 절대 하지 말 것



# ex : 1부터 9까지 모든 정수의 합 구하기 예제 (while문)

i=1
result=0

while i<=9:
    result += i
    i += 1

print(result)

# ex : 1부터 9까지 홀수 합 구하기 예제 (while 문

i=1
result = 0

while i<=9:
    if i % 2 ==1:
        result += i
    i += 1

print(result)

# 무한 루프 : 끊임없이 반복되는 반복 구문 의미
# 반복문을 작성한 뒤에는 항상 반복문을 탈출할 수 있는지 확인할 것



##########################################################################

# for문

#구조
#for 변수 in list:
#   실행할 소스코드


array =[9, 8, 7, 6, 5]

array=(1,2,3,4,5)

for x in array:
    print(x)

# for문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용
# 이때 range(시작 값, 끝 값 + 1) 형태로 사용함.
# 인자를 하나만 넣으면 자동으로 시작 값은 0이 됨

result = 0

for i in range(1, 10):
    result += i

print(result)

# continue 키워드
# 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 continue 사용
# ex : 1부터 9까지의 홀수의 합을 구할 때

result = 0

for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i

print(result)

# break 키워드
# 반복문을 즉시 탈출하고자 할 때 break 사용
# 1부터 5까지의 정수를 차례대로 출력하고자 할 때 다음과 같이 작성 가능

i = 1

while True:
    print('현재 i의 값:', i)
    if i == 5:
        break
    i += 1

# ex 학생들의 합격 여부 판단 예제 : 점수가 80점만 넘으면 합격


scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >=80:
        print(i+1, '번 학생은 합격입니다.')

# 특정 번호의 학생은 제외하기

cheating_student_list ={2, 4}

for i in range(5):
    if i+1 in cheating_student_list:
        continue
    if scores[i]>=80:
        print(i+1, '번 학생은 합격입니다.')

# 중첩된 반복문

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i*j)
    print()