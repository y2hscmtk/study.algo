#첫쨰 줄에 N,M,K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
#둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단 각각의 자연수는 1이상 10000이하의 수로 주어진다.
#입력으로 주어지는 K는 항상 M보다 작거나 같다.
#첫쨰 줄에 동빈이의 큰수의 법칙에 따라 더해진 값을 출력한다.

#동빈이의 큰 수의 법칙은 다음과 같다.
#다양한 수로 이루어진 배열이 있을 떄, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.  
#단, 배열의 특정한 인덱스에 해당하는 수가 연속하여 K번을 초과하여 더해질수 없다.
#예를 들어 2,4,5,4,6으로 이루어진 배열이 있을 떄, M이 8이고 K가 3이라고 가정하자
#이때 특정한 인덱스의 수가 연속해서 세번까지 더해질수 있으므로 큰수의 법칙에 따른 결과 6+6+6+5+6+6+6+5=46이므로, 큰수는 46이 된다.
#만약 숫자가 같을때, 인덱스의 번호가 다르다면 연속하여 더하는것 또한 가능하다.

#아이디어 : N개의 자연수를 리스트 형태로 구분한후, 오름차순으로 정리한다. 
#가장 큰 수를 K번 더하는것이 제일 좋으므로, data[N-1]번째의 데이터를 K번 더한다.
#두번째로 큰 수를 한 번 더한후, 남은 더하기 횟수를 초과하지 않으면서 K를 초과하지 않는만큼 더한다.
#위 과정을 더하기 횟수를 초과하지 않을 때 까지 반복한다.

#공백을 구분하여 세 수를 입력받는다. map()함수는 ()안의 함수에 대해 같은 조건을 적용시키는 역할을 한다
N, M, K = map(int,input().split())

#N개의 수를 공백으로 구분하여 입력받은 후, list형태로 저장한다
data = list(map(int,input().split()))
data.sort() #리스트를 정렬시킨다.



