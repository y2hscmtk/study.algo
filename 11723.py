# https: // www.acmicpc.net/problem/11723

# 백준 11723번
'''
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 
'''

'''
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.
'''

m = int(input())
s = []

# m번의 연산 시행
for _ in range(m):
    data = input().split()
    order = data[0]
    if order != "all" and order != "empty":
        x = int(data[1])
    # S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    if order == "add":
        if x in s:
            continue
        s.append(x)
    # S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    elif order == "remove":
        if x not in s:
            continue
        s.remove(x)
    #  S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    elif order == "check":
        if x in s:
            print(1)
        else:
            print(0)
    # S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    elif order == "toggle":
        if x in s:
            s.remove(x)
        else:
            s.append(x)
    # S를 {1, 2, ..., 20} 으로 바꾼다.
    elif order == "all":
        s = [i for i in range(1, 21)]
    # S를 공집합으로 바꾼다.
    elif order == "empty":
        s = []
