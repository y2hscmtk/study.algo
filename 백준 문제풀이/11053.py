# https://www.acmicpc.net/problem/11053

'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

'''

'''
아이디어 : 입력받은 배열을 정렬시킨후 dp테이블에 값을 기록한다
만약 dp 테이블에 같은 숫자가 존재한다면 해당 요소는 무시하고 다음 값부터 탐색한다.
'''
