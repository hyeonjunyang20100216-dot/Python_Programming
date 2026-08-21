a = 2
b = 3
print(a,end=' ')
print(b)
print(a,b,sep=',')

a = 2;b = 3
#a = (2,b) = 3

x = y = z = 0
a,b = 2,3 #튜플 언패킹
print(a,b)

#값 swap
temp = a
a = b
b = temp
print(a,b)

a,b = b,a

#변수명
#CamelCase, snake_case
snake_case = "뽀로로"
camelCase = "뽀로로"
MAX_VALUE = 100