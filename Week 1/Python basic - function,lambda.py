# 함수

# 특정한 작업을 하나의 단위로 묶어 놓은 것을 의미
# 함수를 사용하면 불필요한 소스코드의 반복을 줄일 수 있음.

# 종류
# 내장 함수 : 파이썬이 기본적으로 제공하는 함수
# 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

# 프로그램에는 똑같은 코드가 반복적으로 사용되어야 할 때가 많음
# 함수를 사용하면 소스코드의 길이를 줄일 수 있음
# 매개변수 : 함수 내부에서 사용할 변수
# 반환 값 : 함수에서 처리 된 결과를 반환

#def 함수명(매개변수):
#   실행할 소스코드
#   return 반환 값

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

print(add(3, 7))
print(subtract(3, 7))


# global 키워드
# global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 됨

a = 0

def func():
    global a
    a+=1

for i in range(10):
    func()

print(a)

array = [1, 2, 3, 4, 5]

def func():
    array.append(6)
    print(array)

func()

def func1():
    array=[]
    array.append(6)
    print(array)

func1()

print(array)

# 여러 개의 반환 값
# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있음

def operator(a, b):
    add_var = a+b
    subtract_var = a-b
    multiply_var = a*b
    divide_var = a/b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(3, 5)

print(a, b, c, d)


# 람다 표현식
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징

print((lambda a, b: a+b)(3, 7))

#(lambda 매개변수: 리턴값)(매개변수 값)

#ex : 내장 함수에서 자주 사용되는 람다 함수

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

# ex: 여러개의 리스트에 적용

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)

print(list(result))

