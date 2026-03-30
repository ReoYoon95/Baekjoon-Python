# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.


T = int(input())

for i in range(T):
    A, B = map(int, input().split())

    if 0 < A < 10 and 0 < B < 10:
        print(A + B)


# 리스트 컴프리헨션
T = int(input())

# 1. 리스트 컴프리헨션으로 계산 결과만 쏙쏙 모으기
# (A+B를 해라 / T번 반복하면서 / 만약 조건에 맞으면)
results = [
    A + B
    for _ in range(T)
    for A, B in [map(int, input().split())]
    if 0 < A < 10 and 0 < B < 10
]

# 2. 모아진 결과 출력하기
for res in results:
    print(res)


# 바다 코끼리를 이용한 리스트 컴프리헨션.
T = int(input())

results = [
    val[0] + val[1]  # 3. 마지막에 더하기 계산!
    for _ in range(T)  # 1. T번 반복하면서
    if (val := list(map(int, input().split())))  # 2. 여기서 val을 만들고 대입!
    and 0 < val[0] < 10
    and 0 < val[1] < 10  # 4. 그 val의 범위를 체크
]

for res in results:
    print(res)
