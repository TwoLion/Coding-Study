# 백준 2941

# 문제

# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
# tilde c : c=
# c' : c-
# dztilde : dz=
# d arrow : d-
# lj : lj
# nj : nj
# tilde s : s=
# tilde z : z=

# 예를 들어, ljes = njak은 크로아티아 알파벳 6개 (lj, e, tildes, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아
# 알파벳으로 이루어져 있는지 출력한다.
# dztilde는 무조건 하나의 알파벳으로 쓰이고, d와 tildez가 분리된 것으로 보지 ㅏㅇㄶ는다. lj와 nj도 마찬가지이다. 위 목록에 없는
# 알파벳은 한 글자씩 센다.

# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력된다.

sentence = list(input())
sentence.append('')
sentence.append('')
count = 0

for i in range(len(sentence)):
    if sentence[i] == '-' or sentence[i] =='=' or sentence[i]=='':
        pass
    elif sentence[i]=='n' :
        if sentence[i+1] =='j':
            pass
        else :
            count +=1

    elif sentence[i]=='l' :
        if sentence[i+1] == 'j':
            pass
        else:
            count += 1
    elif sentence[i]=='d' :
        if sentence[i+1] =='z' and sentence[i+2]=='=':
            pass
        else:
            count +=1
    else:
        count +=1

print(count)