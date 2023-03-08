# https://www.acmicpc.net/problem/10971
'''
각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. 

W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 

비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다. 

모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다. 

경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.
'''
