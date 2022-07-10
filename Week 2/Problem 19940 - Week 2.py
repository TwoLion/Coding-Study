# 백준 19940

# 문제

# 피자를 굽는 전자식 오븐이 있다. 이 오븐에 재료는 넣고 정확히 N분 동안 동작을 시키고자 한다. 그런데 이 오븐에 준비된 버튼은 동작 시간을 추가시키거나 감소시킨다. 처음에 피자 오븐의 첫 시간은 0분으로 정해져 있다. 시간을 감소시키는 버튼을 눌러서 시간이 0분보다 작아지는 경우에는 0분으로 설정된다. t가 현재 오븐에 세팅된 시간, t'은 버튼을 누른 뒤의 시간을 의미할 때, 각 버튼은 다음과 같은 기능을 가지고 있다.

# ADDH : t' = t + 60
# ADDT : t' = t + 10
# MINT : t' = t - 10
# ADDO : t' = t + 1
# MINO : t' = t-1

# 설정해야할 시간이 주어졌을 때, 그 시간을 만들기 위해 눌러야 하는 버튼의 최소 횟수와 그 방법을 구하는 프로그램을 작성하시오.

# 입력 : T개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 설정해야 하는 시간 N이 정수로 주어진다.

# 출력 : 각각의 테스트 케이스마다 5개의 정수를 한 줄에 공백으로 구분해서 출력한다. 이 정수는 입력으로 주어진 시간을 만들기 위해서 ADDH, ADDT, MINT, ADDO, MINO 버튼을 누르는 횟수를 출력한 것이다. 최소 횟수로 누르는 방법이 여러가지인 경우에는 사전 순으로 가장 앞서는 방법을 출력한다.
# 작업 횟수가 동일한 방법이 여러가지가 있을 때, ADDH를 누르는 횟수가 적은 것이 사전 순으로 앞서는 것이고, ADDH를 누르는 횟수가 동일하면, ADDT를 누르는 횟수가 적은 것이 먼저이다. ADDT를 누르는 횟수가 동일하면 MINT를 누르는 횟수가 적은 것이, MINT를 누르는 횟수가 동일하면 ADDO를 누르는 횟수가 적은 것이, ADDO를 누르는 횟수가 동일하면 MINO를 누르는 횟구가 적은 것이 사전 순으로 앞서는 것이다.


T = int(input())

oventime = []

for _ in range(T):
  oventime.append(int(input()))



def count_check(t):
  
  time_list = [0, 0, 0, 0, 0]
  
  remain = t

  result_hour = remain//60
  remain = remain%60

  time_list[0]=result_hour

  if remain % 10 >=5:

    if remain // 10 == 5 :
      time_list[0] += 1
      time_list[4] += 10-remain%10

    elif remain // 10 == 4 :
      time_list[0] += 1
      time_list[2] += 1
      time_list[4] += 10-remain%10

    elif remain // 10 == 3 :
      if remain == 35:
        time_list[1] +=3
        time_list[3] +=5
      else:
        time_list[0] +=1
        time_list[2] +=2
        time_list[4] +=10-remain%10

    else:
      if remain % 10 == 5:
        time_list[1] += remain//10
        time_list[3] += remain%10
      else:
        
        time_list[1] += remain//10 +1
        time_list[4] += 10-remain%10

  else:
    if remain//10 ==5 :
      time_list[0] += 1
      time_list[2] += 1
      time_list[3] += remain% 10

    elif remain//10 == 4 :
      time_list[0] += 1
      time_list[2] += 2
      time_list[3] += remain%10

    else:
      time_list[1] += remain//10
      time_list[3] += remain %10

  return(time_list)

    
    
result = list(map(count_check, oventime))

for i in range(len(result)):
  for j in range(5):
    print(result[i][j], end=' ')
  print()
  
