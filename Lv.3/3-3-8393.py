# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.

n = int(input())
total = 0
for num in range(1, n + 1):
    total += num
print(total)


# 만약 리스트 컴프리헨션을 쓴다면?? 좋은 코드는 아님.

n = int(input())

# 1. [1, 2, 3, ..., n] 이 담긴 리스트를 만듭니다.
numbers = [num for num in range(1, n + 1)]

# 2. 내장 함수 sum()으로 리스트 안의 모든 숫자를 더합니다.
print(sum(numbers))

# 한 줄로 합치면?
# print(sum([num for num in range(1, n + 1)]))


# 베스트 코드.
n = int(input())
print(sum(range(1, n + 1)))
