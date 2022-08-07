# 피보나치 수열 소스 코드
# 점화식 함수 만드는 방법

def fibo(x):
    if x==1 or x==2:
        return 1

    else:
        return fibo(x-1)+fibo(x-2)

print(fibo(4))


# 탑다운 다이나믹 프로그래밍 코드

d = [0]*100

def fibo(x):
    if x ==1 or x ==2 :
        return 1
    if d[x]!=0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))


# 바텀업 다이나믹 프로그래밍 코드

d = [0]*100

d[1] =1
d[2] = 1
n=99

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])

# 메모이제이션 과정

d = [0]*100

def fibo(x):
    print('f(' + str(x) +')', end=' ')
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]

    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]


fibo(6)