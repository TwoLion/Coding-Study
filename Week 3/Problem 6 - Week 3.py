# Q08 : 문자열 재정렬

# 문제

# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

# 입력 조건 : 첫째 줄에 하나의 문자열 S가 주어집니다. (1<=S의 길이<=10,000)
# 출력 조건 : 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

a = list(input())

num = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

count = 0
alphabet =[]

for i in range(len(a)):
    if a[i] in num:
        count += int(a[i])

    else:
        alphabet.append(ord(a[i]))

alphabet.sort()

alphabet = list(map(chr, alphabet))


for i in alphabet:
    print(i, end='')

print(count, end='')