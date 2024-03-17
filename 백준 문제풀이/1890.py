# https://www.acmicpc.net/problem/1890
'''
가장 오른쪽 아래 칸으로 이동하는 것이 목표
각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미한다. 반드시 오른쪽이나 아래쪽으로만 이동해야 한다. 
0을 만나면 더 이상 이동할 수 없음 => 종착점(점프 가능한 거리가 0임)
항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야 한다. 한 번 점프를 할 때, 방향을 바꾸면 안 된다.
즉, 한 칸에서 오른쪽으로 점프를 하거나, 아래로 점프를 하는 두 경우만 존재한다.
가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 이동할 수 있는 경로의 개수를 구하는 프로그램을 작성하시오.

dp[i][j] (1,1)에서 (i,j)까지 올 수 있는 방법의 수
현재 칸에서 오른쪽 칸과 오른쪽 아래 칸으로 이동 할 수 있는 조건 
1. 현재칸(arr[i][j])이 0이 아니어야함 
2. 현재 칸으로 올 수 있는 방법이 있어야함 dp[i][j] != 0 # 방법이 있어야함
'''
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1 # 시작칸으로 갈 수 있는 방법은 무조건 존재 함
for i in range(n):
    for j in range(n):
        # 현재 칸으로 올 수 있는 방법이 존재하는지 확인
        if dp[i][j] != 0 and arr[i][j] != 0: # 현재 칸에서 점프 할 수 있는지 확인
            for dx,dy in ((0,1),(1,0)): # 오른쪽 혹은 아래로만 이동 가능
                nx = i + arr[i][j]*dx; ny = j + arr[i][j]*dy # 다음에 이동하게 될 칸
                if 0<=nx<n and 0<=ny<n: # 영역 확인
                    dp[nx][ny] += dp[i][j] # 이전 칸에 도달 할수 있는 경우의 수 누적
print(dp[n-1][n-1]) # (n,m)으로 갈 수 있는 방법의 수 출력