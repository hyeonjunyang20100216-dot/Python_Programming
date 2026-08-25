#입출력 처리

# a = input()
# print(a)
# print(type(a))

#정수로 변환
a = input()
a = int(a)
print(a,type(a))

a = int(input())
print(a,type(a))

#실수입력
a = float(input())
print(a,type(a))

# a = int(input())
# b = int(input())
# print(a,b)

#100 200
# a = input().split()
# print(a,type(a))

#map(함수, 리스트)
a, b, c = map(int,input().split())
print(a,type(a))
print(b,type(b))
print(c,type(c))

#리스트 변환
a = list(map(int,input().split()))
print(a,type(a))