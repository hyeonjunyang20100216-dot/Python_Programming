# 튜플 심화

# ===========================================================
#  튜플에서 제공하는 메소드
# ===========================================================

t = (1, 1, 2, 2, 2)

print(t.count(1))                    # 1이 몇개 있는지?

print(t.index(2))                    # 2의 첫번째 인덱스는?


# ===========================================================
#  그 외
# ===========================================================

# tuple -> list 변환
lst = list(t)
print(lst)

# list -> tuple 변환
tup = tuple(lst)
print(tup)

# 튜플을 이용해서 swap하기
a, b = 10, 20
a, b = b, a
print(a, b)

# 튜플 언패킹
t = (1, 2, 3, 4)
t2 = (5, 6)
a, b, c, d = t
print(*t, *t2)  # 1 2 3 4 5 6


# zip 함수 사용
subjects = ("국어", "수학", "영어")
scores = (80, 90, 95)

# (('국어', 80), ('수학', 90), ('영어', 95)) 출력하기
result = tuple(zip(subjects, scores))
print(result)


# ===========================================================
#  Tuple Comprehension은 없음
# ===========================================================

#generator 표현식 사용
gen = (x for x in range(1, 11))
print(next(gen))
print(next(gen))

# generator는 한 번 순회하면 끝나므로 다시 순회하려면 새로 생성해야 함
for i in gen:
    print(i, end=" ")
print()

for i in gen:
    print(i, end=" ") 
print()
#List Comprehension vs Generator Expression
a = [x for x in range(1, 11)]  # List Comprehension
b = (x for x in range(1, 11))  # Generator Expression
print(a)
print(b)

print(sum(a),sum(a))
print(sum(b),sum(b))




# 1 ~ 10의 제곱수 튜플 만들기
# ()는 튜플이 아니라 generator를 생성하는 generator 표현식임
gen = (i ** 2 for i in range(1, 11))
print(gen)

# tuple의 생성자에 generator를 넘겨 값을 순회하면서 튜플을 만듦
sq_tuples = tuple(i ** 2 for i in range(1, 11))
print(sq_tuples)

# 두 점의 x, y, z축 좌표값끼리 더한 튜플을 만들기
p1 = (1, 2, 3)
p2 = (10, 20, 30)
p3 = tuple(x + y for x, y in zip(p1, p2))
print(p3)


# =========================================================
#  🔥 실습 문제
# =========================================================

# 일주일 동안의 학습 시간을 저장한 튜플
days = ("일","월","화","수","목","금","토")
hours = (2, 3, 1, 4, 5, 2, 6)

# 1️⃣ 월 ~ 금까지 총 학습시간 출력하기
print(f"{sum(hours[1:6])}시간")                     # ✅ 15시간


# 2️⃣ 가장 많이 공부한 시간 출력하기
print(f"{max(hours)}시간")                        # ✅ 6시간


# 3️⃣ 가장 많이 공부한 요일 출력하기
max_idx = hours.index(max(hours))
print(f"{days[max_idx]}요일")                      # ✅ 토요일


# 4️⃣ 가장 높은 점수와 가장 낮은 점수 출력하기
scores = (90, 85, 78, 92, 88, 76)

print(f"max 점수: {max(scores)}점, min 점수: {min(scores)}점") # ✅ max 점수: 92점, min 점수: 76점

res = sorted(scores)

print(f"max 점수: {res[-1]}점, min 점수: {res[0]}점") # ✅ max 점수: 92점, min 점수: 76점

# 5️⃣ 과일가게 총 재고 금액 구하기
stocks = (
    ("사과", 1000, 5),
    ("바나나", 2000, 3),
    ("체리", 5000, 2),
)

# 총 재고 금액 출력
total = sum(price * count for item, price, count in stocks)
total = sum([price * count for item, price, count in stocks])
print(f"총액: {total:,}원")                        # ✅ 총액: 21,000원  

