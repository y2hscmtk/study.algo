# https://www.acmicpc.net/problem/2231
'''
문제
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 

어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 

따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.
'''
import sys
n = int(input())

# 생성자가 없는 경우에는 0을 출력한다.
# 어떤수이든, 생성자는 분해합보다 작을 것이므로, n만큼 반복하면 된다.
for i in range(1, n+1):
    temp = i  # i의 분해합을 구하기 위해,
    for num in str(i):
        temp += int(num)  # 각 자리수를 더한다.
    if temp == n:  # i의 분해합이 n이 된다면, 즉 i가 n의 생성자라면
        print(i)  # i를 출력하고 프로그램을 종료한다.
        sys.exit(0)

print(0)  # 생성자가 없는경우 0을 출력한다.
