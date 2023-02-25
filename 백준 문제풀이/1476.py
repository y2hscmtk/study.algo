# https://www.acmicpc.net/problem/1476
'''
준규가 사는 나라는 우리가 사용하는 연도와 다른 방식을 이용한다. 

준규가 사는 나라에서는 수 3개를 이용해서 연도를 나타낸다. 각각의 수는 지구, 태양, 그리고 달을 나타낸다.

지구를 나타내는 수를 E, 태양을 나타내는 수를 S, 달을 나타내는 수를 M이라고 했을 때, 

이 세 수는 서로 다른 범위를 가진다. (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)

우리가 알고있는 1년은 준규가 살고있는 나라에서는 1 1 1로 나타낼 수 있다. 

1년이 지날 때마다, 세 수는 모두 1씩 증가한다. 만약, 어떤 수가 범위를 넘어가는 경우에는 1이 된다.

예를 들어, 15년은 15 15 15로 나타낼 수 있다. 하지만, 1년이 지나서 16년이 되면 16 16 16이 아니라 1 16 16이 된다.

이유는 1 ≤ E ≤ 15 라서 범위를 넘어가기 때문이다.

E, S, M이 주어졌고, 1년이 준규가 사는 나라에서 1 1 1일때, 준규가 사는 나라에서 E S M이 우리가 알고 있는 연도로 몇 년인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 세 수 E, S, M이 주어진다. 문제에 나와있는 범위를 지키는 입력만 주어진다.

출력
첫째 줄에 E S M으로 표시되는 가장 빠른 연도를 출력한다. 1 1 1은 항상 1이기 때문에, 정답이 음수가 나오는 경우는 없다.
'''
'''
1년부터 ESM으로 수를 표기하여 점점 수를 올려나간다.
만약 데이터로 주어진 ESM과 동일한 수를 발견하면 반복을 종료하고 정답을 출력한다.
'''
# esm년도 입력받기
esm = list(map(int, input().split()))

year = 1  # 실제로 몇년인지 저장할 변수

# 초기 데이터 1년차일때 esm의 모습
data = [1, 1, 1]

# 원하는 값을 찾을때까지 반복
while True:
    # esm과 같은 년도를 찾았다면 반복 종료
    if data == esm:
        break
    else:
        year += 1  # 년차를 더하고 esm의 범위 조건에 맞춰 수를 늘려나간다.
        for i in range(3):
            data[i] += 1
        # 값이 범위를 넘어서면 1로 변경되도록
        # 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
        data[0] = 1 if data[0] == 16 else data[0]
        data[1] = 1 if data[1] == 29 else data[1]
        data[2] = 1 if data[2] == 20 else data[2]


# 정답 출력
print(year)
