# 알바로 부자 되기
'''
일하는 기간이 겹치지 않게 하면서 얻을 수 있는 돈이 최대가 되도록 하는 프로그램 작성
동시에 2개 이상의 알바를 하는 것은 불가능
각각의 알바는 일해야 하는 기간을 모두 채워야한다.
알바를 끝낸 날과 다른 알바를 시작하는 날이 일치하는 경우도 일하는 기간이 겹치는 것으로 간주
'''
n = int(input())

alba = []
for _ in range(n):
    # 알바 시작, 끝나는 날, 얻게 되는 돈
    s,e,p = map(int,input().split())
    alba.append((s,e,p))

# 알바 시작하는 날짜 순으로 정렬하여 데이터가 주어지므로, 별도의 정렬 필요x

dp = [0]*n # dp[i] : i번째 알바 선택시 얻을 수 있는 최대 금액
# O(N^2)
for i in range(n):
    # 이전 알바들 중 현재 알바와 겹치지 않는 알바를 선택한 상황과 현재 알바를 이어서 하는 경우 생각
    s_i,e_i,p_i = alba[i]
    # 이전에 알바를 하지 않는다면 현재 시점에서의 최대 이득은 현재 알바에 대한 금액
    dp[i] = p_i
    # j알바는 이전 알바들
    # i알바의 시작 일자가 j알바의 종료 일수보다 앞서있어야 선택가능
    for j in range(i):
        s_j,e_j,p_j = alba[j]
        if e_j < s_i: # 이러한 경우에만 알바 선택 가능
            dp[i] = max(dp[i], dp[j] + p_i) # 이전 알바 + 현재 알바 이득
    
ans = 0
for i in range(n):
    ans = max(ans,dp[i])

print(ans)