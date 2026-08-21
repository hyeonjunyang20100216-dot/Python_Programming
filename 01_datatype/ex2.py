#파이썬 자료형
#1. 기본 자료형 : 숫자형(정수,실수) ,불리언,문자열
#2. 컬렉션 자료형 : 리스트, 튜플, 딕셔너리, 집합

#숫자형
a = 10
print(type(a))
#2진수, 8진수, 16진수
print(bin(a),oct(a),hex(a))
print(ord('A'),chr(65))

#int 자료형은 값 의 표현 범위가 제한 X
x = 10 ** 100
print(x,type(x))

#오버플로우 테스트
a  = 2147483647 + 1
print(a,type(a))

b = 3.14
print(b,type(b))

import sys
print(sys.float_info.min)
print(sys.float_info.max)

print(-sys.float_info.max)
print(-sys.float_info.min)

a = 1.7e308
b = 1.8e308
print(a,type(a))
print(b,type(b))

print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.3:.20f}")
