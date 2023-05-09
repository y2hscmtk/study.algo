# https://www.acmicpc.net/problem/1072
'''
게임 기록은 다음과 같이 생겼다.
게임 횟수 : X
이긴 게임 : Y (Z%)
Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.
'''
'''
이분탐색
mid에서 승률이 변화하였다면, 더 낮은 횟수로도 승률이 변했는지 탐색해야하므로
high를 mid로 바꾸어 다시 탐색을 진행한다.
mid에서 승률이 변화하지 않았다면, 더 많은 게임을 해야한다는 것을 의미하므로
low를 mid+1로 바꾸어 다시 탐색을 진행한다.
'''
# 승률 z는 (y/x)*100이다.
# Z는 형택이의 승률이고, 소수점은 버린다. 예를 들어, X=53, Y=47이라면, Z=88이다.
x, y = map(int,input().split()) # x,y 입력받기

# 초기 승률 기록
z = (y*100)//x


# 승률 계산함수 작성
def change(game): # 게임의 횟수를 매개변수로 보내어 승률변화가 발생하였는지 확인
    # 형택이는 모든 게임에서 '지지 않는다'
    if z != ((y+game)*100)//(x+game): # (이긴횟수/전체 게임횟수) * 100
        # 승률의 변화가 발생하였다면
        return True
    else:
        return False
    
    
result = -1
# 승률에 변화가 발생하였는지 이분탐색을 통해 확인
# 만약 Z가 절대 변하지 않는다면 -1을 출력한다.
# 승률이 변화하지 않는 경우는 이미 승률이 100퍼센트일때를 제외하고 없다.
# (매판 게임에서 승리하므로 승률이 떨어질일도 없다.)
# 초기에 승률이 백퍼센트인지 확인하고, 그렇다면 이분탐색을 시행하지 않는다.
if x==y:
    print(result)
else: # 승률이 백퍼센트가 아니라면 승률변화가 무조건 발생한다.
    # 지금까지 게임을 한만큼 더 이긴다면 승률변화는 무조건 발생할것이다.
    # 따라서 high는 최대 게임 횟수인 1,000,000,000으로 설정한다.
    low,high = 1,1000000000
    while low<high:
        mid = (low+high)//2
        if change(mid): # 변화가 발생했다면 => 더 적은 횟수로도 승률변화가 발생할수있는지 확인
            high = mid
            result = mid
        else: # 승률변화가 없다면 탐색범위를 mid보다 높게 설정해야함
            low = mid+1
    print(result)