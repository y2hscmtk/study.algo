# https://www.acmicpc.net/problem/3190

# 백준 3190번 구현 알고리즘 문제

#  'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
#  뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# 입력

# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며.

# 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.


# 빈 공간은 0, 사과는 1, 뱀이 지나간 경로는 2로 표현한다. 뱀의 머리는 3으로 표현한다.
# 뱀의 이동경로를 조작하기 위한 리스트, 방향은 북 동 남 서 순으로 이동한다.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# d = [0, 1, 2, 3]  # 현재 뱀의 머리가 바라보는 방향 북 동 남 서 방향순
time = 0  # 뱀이 이동한 시간

n = int(input())  # 경기판의 크기 n x n

array = [[0]*n for _ in range(n)]  # n x n크기의 게임판 생성

k = int(input())  # 사과의 개수를 의미

for _ in range(k):  # k번 반복하여, 사과를 놓을 위치 설정
    # 공백으로 구분하여 사과를 놓을 위치 array[r][c]를 입력받는다
    row, column = map(int, input().split())
    array[row][column] = 1  # 사과가 존재하는 장소는 1로 표현한다.

l = int(input())  # 뱀이 회전하는 횟수

t = []
turn = []  # 뱀이 회전하는 시간, 방향에 대한 정보 저장 (시간,방향(L은 왼쪽으로 90도, D는 오른쪽으로 90도 회전))

for i in range(l):
    data = input().split()
    t.append(int(data[0]))
    turn.append(data[1])

# 뱀의 머리
array[0][0] = 3
direction = 1  # 뱀은 처음에 오른쪽을 향한다.
r, c = 0, 0  # 뱀의 초기 위치
body = 0  # 몸통의 길이
# 뱀의 꼬리
tr, tc = r, c

while True:
    # time += 1  # 뱀은 매 초마다 움직임을 수행한다.
    # 뱀이 회전을 하는지 확인
    # 회전한다면, 방향을 바꿔 사과 찾기 알고리즘을 수행
    if time in t:  # 해당 시간에, 뱀이 회전을 한다면
        at = t.index(time)
        if turn[at] == 'L':
            direction -= 1
            if direction == -1:
                direction = 3
            # direction = d[direction-1]  # 왼쪽으로 90도 회전
        elif turn[at] == 'D':
            direction += 1
            if direction == 4:
                direction = 0
            # direction = d[direction+1]  # 오른쪽으로 90도 회전
    # 회전하지 않는다면, 현재 방향으로 계속 이동하며 사과 찾기 알고리즘을 수행

    # 빈 공간 0 사과 1 뱀의 이동경로 2 뱀의 머리 3
    # 뱀이 바라보는 방향으로 한 칸 이동

    # 뱀의 임시 머리칸
    ar = r + dr[direction]
    ac = c + dc[direction]

    # 영역을 벗어나지 않았는지 확인
    if ar < 0 or ar >= n or ac < 0 or ac >= n:
        time += 1
        break
    if array[ar][ac] == 1:  # 사과가 있다면?
        body += 1  # 몸 길이 +1
        array[r][c] = 2  # 머리를 몸으로 변경
        array[tr][tc] = 3  # 꼬리 설정
    elif array[ar][ac] >= 2:  # 몸과 부딛힐경우
        time += 1
        break
    elif array[ar][ac] == 0:  # 사과가 없는 빈 공간으로 이동할 경우
        # 머리를 앞으로 이동한 후, 머리와 몸까지의 영역을 몸으로 변경하는 작업 필요 => 머리와 몸이 분리될수 있음
        # 방향에 따라서 작업 실행
        if direction == 0:
            for i in range(1, body+1):
                array[ar-i][ac] = 2
            array[tr][tc] = 0  # 꼬리가 있던 위치를 빈 공간으로 변경
            tr = tr+1
        elif direction == 1:
            for i in range(1, body+1):
                array[ar][ac-i] = 2
            array[tr][tc] = 0  # 꼬리가 있던 위치를 빈 공간으로 변경
            tc = tc+1
        elif direction == 2:
            for i in range(1, body+1):
                array[ar+i][ac] = 2
            array[tr][tc] = 0  # 꼬리가 있던 위치를 빈 공간으로 변경
            tr = tr-1
        elif direction == 3:
            for i in range(1, body+1):
                array[ar][ac+i] = 2
            array[tr][tc] = 0  # 꼬리가 있던 위치를 빈 공간으로 변경
            tc = tc-1
    time += 1
    r = ar
    c = ac  # 다음칸으로 이동
    array[r][c] = 3  # 머리 이동

print(time)