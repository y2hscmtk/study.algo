#p.87 거스름돈 문제
#거스름돈으로 사용할 500원,100원,50원,10원짜리 동전이 무한히 있다고 가정한다.
#손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라.

#그리디 알고리즘은 현재의 선택이 나중에 미칠 영향에 대해 고려하지 않고, 현재 상황에서의 최선의 선택을 하는것이다.

#문제상황에서 N원짜리 동전을 최소한으로 거슬러주기 위해선, 최고 화폐단위(500원)으로 최대한 많이 거슬러 줘야 할것이다.

#사용자로부터, 금액을 입력받는다
n = int(input())
count = 0

coin_type = [500,100,50,10]

for coin in coin_type:
    count += n//coin #금액을 동전으로 나눈 몫을 count에 할당
    n%=coin #금액을 동전으로 나눈 나머지 값을 다시 n으로 초기화

print(count)
