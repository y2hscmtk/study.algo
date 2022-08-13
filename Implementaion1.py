# 구현 알고리즘 : 머리솟에 있는 알고리즘을 소스코드로 바꾸는 과정, 거의 모든 범위의 코딩 테스트 문제 유형을 포함한다.
# 프로그래밍 언어의 문법을 정확히 알고 있어야 하며, 문제의 요구사항에 어긋나지 앟는 답안 코드를 실수 없이 작성해야 한다.
# 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제, 특정 소수점 자리까지 출력해야 하는 문제, 문자열이 입력으로 주어질때 한 문자 단위로 끊어서 리스트에 넣어야 하는 문제,등
# 경험이 많다면 쉬울 수 있으나, 초보자 입장에서 어렵게 느껴질 수 있다.
# 다수의 라이브러리 경험이 필요, 완전 탐색과 시뮬레이션 둘 다 포함하고 있다.

# 고려해야 할 것 : 메모리 제약 사항

# 문제 : 상하좌우
# N X N 크기의 정사각형 공간위에 서 있을때, 이 공간은 1x1크기의 정사각혀응로 나누어져 있다. 가장 왼졲 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당한다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D 중의 하나의 문자가 반복적으로 적혀 있으며 그 의미는 다음과 같다.
# L : 왼쪽으로 한 칸 이동 R: 오른쪽으로 한 칸 이동 U: 위로 한 칸 이동 D: 아래로 한 칸 이동
# 이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.

# 입력 조건 : 첫째 줄에 공간의 크기를 나타내는 N이 주어진다.
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다.

# 출력 조건 :첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (x,y)를 공백으로 구분하여 출력한다.

n = int(input())

x, y = 1, 1 # x, y 초기 좌표 설정

data = list(input().split())

for i in data:
    if i=='R':
        y+=1
        print(x,y)
    elif i=='L':
        y-=1
        print(x,y)
    elif i=='U':
        x-=1
        print(x,y)
    elif i=='D':
        x+=1
        print(x,y)
    # x,y 좌표가 정해진 영역 밖으로 이동할경우 고려
    if x==0:
        x+=1
    if x>n:
        x-=1
    if y==0:
        y+=1
    if y>n:
        y-=1

print(x,y)

