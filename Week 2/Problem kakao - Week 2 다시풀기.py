# 문제

# 회전판에 먹어야 할 N개의 음식이 있습니다. 각 음식에는 1부터 N까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요됩니다. 무지는 다음과 같은 방법으로 음식을 섭취합니다.
#1. 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓습니다.
#2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 옵니다.
#3. 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취합니다. 다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말합니다.
#4. 회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정합니다.

# 무지가 먹방을 시작한 지 K초 후에 네트워크 장애로 인해 방송이 잠시 중단되었습니다. 무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 합니다. 각 음식을 모두 먹는 데 필요한 시간이 담겨 있는 배열 Food_times, 네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return하도록 solution 함수를 완성하세요

# 제한 사항
# 1. food_times는 각 음식을 모두 먹는 데 필요한 시간이 음식의 번호 순서대로 들어있는 배열입니다.
# 2. k는 방송이 중단된 시간을 나타냅니다.
# 3. 만약 더 섭츃해야 할 음식이 없다면 -1을 반환하면 됩니다.

# 정확성 테스트 제한 사항
# food_times의 길이는 1 이상 2000 이하입니다.
# food_times의 원소는 1 이상 1000 이하의 자연수입니다.
# k는 1 이상 2000000 이하의 자연수입니다.

# 효율성 테스트 제한 사항
# food_times의 길이는 1 이상 200000 이하입니다.
# food_times의 원소는 1 이상 100000000 이하의 자연수입니다.
# k는 1 이상 2*10^13 이하의 자연수입니다.




def solution(food_times, k):

  result = 0
  
  while k > 0 :

    min_val_list = [i for i in food_times if i not in set([0])]

    if min_val_list==[]:

      result = -1
      break
    
    min_val = min(min_val_list)

    if k-len(min_val_list)*min_val<0:
      break

    else:

      food_times = list(map(lambda x:(x-min_val)*((x-min_val)>=0), food_times))
      k += -len(min_val_list)*min_val
    
    
  comp = 0
  index = 0
  for i in range(len(food_times)):
    if food_times[i]>0:
      comp+=1
      index +=1
    else:
      comp+=1
      pass

    if index == k+1:
      break

  if result==-1:
    comp = -1
  
  

  return(comp)


######## 시부레 다시 하기...