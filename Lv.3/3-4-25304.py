# 문제
# 준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

# 영수증에 적힌,

# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
# 을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

# 입력
# 첫째 줄에는 영수증에 적힌 총 금액
# $X$가 주어진다.

# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수
# $N$이 주어진다.

# 이후
# $N$개의 줄에는 각 물건의 가격
# $a$와 개수
# $b$가 공백을 사이에 두고 주어진다.

# 출력
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.

# 제한
#
# $1 ≤ X ≤ 1\,000\,000\,000$
#
# $1 ≤ N ≤ 100$
#
# $1 ≤ a ≤ 1\,000\,000$
#
# $1 ≤ b ≤ 10$

X = int(input())
N = int(input())

a = 0
b = 0
my_total = 0
for _ in range(N):
    a, b = map(int, input().split())
    my_total += a * b

if X == my_total:
    print("Yes")
else:
    print("No")


# 개선된 방식 데이터를리스트 안의 튜플로 모으기

X = int(input())
N = int(input())

# 1. 정보를 담을 빈 리스트 생성
price_list = []

for _ in range(N):
    # 입력을 받아서 튜플 (a, b) 형태로 리스트에 추가
    a, b = map(int, input().split())
    price_list.append((a, b))

my_total = 0

# 리스트에서 튜플을 하나씩 꺼내서 a와 b에 바로 나눠 담습니다!
for a, b in price_list:
    my_total += a * b

if X == my_total:
    print("Yes")
else:
    print("No")


# 리스트 컴프리헨션 응용

X = int(input())
N = int(input())

# 1. 입력받으면서 바로 (가격 * 개수) 결과값들만 리스트로 만듭니다.
# [2000, 3000, 5000] 이런 식의 리스트가 생기겠죠?
results = [a * b for _ in range(N) for a, b in [map(int, input().split())]]

# 🔍 2. 왜 map을 [ ]로 감싸야 하나요?
# 이게 가장 헷갈리는 부분일 텐데, 파이썬의 for A in B 문법 때문입니다.
# B 자리에는 반드시 **'여러 개가 들어있는 보따리(Iterable)'**가 와야 해요.
# map(...) 자체는 숫자 두 개가 든 보따리처럼 보이지만, 파이썬은 "이 보따리 안에 든 알맹이가 2개니까 a, b로 쪼개라"고 하면 한 번에 한 알맹이씩만 꺼내려고 해서 에러가 납니다.
# 그래서 [map(...)] 처럼 보따리를 통째로 큰 박스에 한 번 더 담아서 넘겨주면, 파이썬이 "아, 이 박스에서 보따리 하나를 꺼내서 a, b로 쪼개면 되겠구나!"라고 이해하게 됩니다.


# 2. 리스트의 모든 값을 합쳐서 X와 비교!
print("Yes" if X == sum(results) else "No")


# price_List = list(map(int, input().split()))

# for p, c in zip(price_List):


# 바다코끼리(대입 표현식) 쓰는 법

results = [(v := list(map(int, input().split())))[0] * v[1] for _ in range(N)]
