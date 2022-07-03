# 조건문 : 프로그램 흐름을 제어하는 문법
# 조건문을 이용해 조건에 따라서 프로그램의 로직 설정 가능
# R과는 달라서 조건을 걸 때 괄호 절대 하지 말 것

x = 15

if x>= 10:
    print("x >= 10")

if x>=0:
    print("x >= 0")

if x>=30:
    print("x>=30")

# 파이썬에서는 코드의 block을 들여쓰기로 지정함.

# 들여쓰기 : 탭을 사용하거나, 스페이스를 여러 번 사용하자 나눌 수 있음
# 파이썬 스타일 가이드라인에서는 4개의 공백문자를 사용하는 것을 표준으로 설정

# 기본 형태 : if, elif, else

#if 조건문 1:
#   조건문 1이 True일 때 실행되는 코드
#elif 조건문 2:
#   조건문 1에 해당하지 않고, 조건문 2가 true일 대 실행되는 코드
#else:
#   조건문1, 2에 해당하지 않을 때 출력되는 코드

a = -15

if a>=0:
    print("a>=0")

elif a>= -10:
    print("0>a>=-10")

else:
    print("-10>a")


# ex

score = 85

if score >=90:
    print('학점:A')
elif score>=80:
    print('학점:B')
elif score>=70:
    print('학점:C')
else:
    print('학점:F')

# 비교 연산자
# X==Y
# X!=Y
# X>Y
# X<Y
# X>=Y
# X<=Y

# 논리 연산자
# X and Y : X와 Y가 모두 참일 때 참이다.
# X or Y : X와 Y 중 하나만 참이어도 참이다.
# not X : X가 거짓일 때 참이다.

if True or False:
    print('Yes')

if True and False:
    print('Yes')

a=15

if a<=20 and a>=0:
    print('Yes')


# 다수의 데이터를 ㅏㄷㅁ는 자료형을 위해 in 연산자와 not in 연산자 사용
# list, tuple, string, dictionary 모두 사용 가능

# x in list : list 안에 x가 들어가 있을 때 참이다.
# not in 문자열 : 문자열 안에 x가 들어가 있지 않을 때 참이다.

# pass
# 아무것도 처리하고 싶지 않을 때 pass 키워드 사용

score = 85

if score >= 80:
    pass
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

a =50

if a>=30:
    pass
else:
    print("a<30")


# 조건문 간소화
# 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현할 수 있음

score = 85

if score >=80: result = "Success"
else: result = 'Fail'

# 조건부 표현식은 if~else 문을 한 줄에 작석할 수 있도록 해줌

score = 85
result = 'Sucess' if score>=80 else 'Fail'

# 파이썬은 조건문 안에서 수학의 부등식 그대로 사용할 수 있음

x = 15
y=20
if x>0 and x<20:
    print('Yes')

if 0<x<y<25:
    print('Yes')