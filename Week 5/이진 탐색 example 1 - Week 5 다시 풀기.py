# 부품 찾기

# 문제

# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을
# 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서
# 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자

# 입력 : 첫째 줄에 정수 N이 주어진다. (1<=N<=1,000,000)
# 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이 때 정수는 1보다 크고 1,000,000 이하이다.
# 셋째 줄에는 정수 M이 주어진다. (1<=M<=100,000)
# 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.

# 출력 : 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.

N = int(input())

product = list(map(int, input().split()))

M = int(input())

need = list(map(int, input().split()))

product.sort()

def finding_product(product, need, start, end):

    mid = (start+end)//2

    if start>end:
        return('no')

    if product[mid]==need:
        return('yes')
    elif product[mid]>need:
        return(finding_product(product, need, start, end=mid-1))
    else:
        return(finding_product(product, need, start=mid+1, end=end))
    return('no')




for i in range(M):
    check = finding_product(product=product, need=need[i], start=0, end=len(product))
    print(check, end=' ')




