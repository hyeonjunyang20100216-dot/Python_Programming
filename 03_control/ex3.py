for i in range(5):
    print(i,end=" ")
print()

a= range(5)
print(a.start, a.stop, a.step)

for i in range(1,6):
    print(i,end=" ")
print()

#1~10, 2씩 띄어서
for i in range(1,11,2):
    print(i,end=" ")
print()


# 5,4,3,2,1
for i in range(5,0,-1):
    print(i,end=" ")
print()

# 1~10까지의 합
tot = 0
for i in range(1,11):
    tot += i
print(tot)

print(sum(range(1,11)))

#1 ~ 10까지의 합 
i = 1
tot = 0
while i <= 10:
    if(i%2==0):
        tot += i
    i += 1
print(tot)

#인코딩
s = "안녕하세요你好"

for c in s:
    print(c, end=" ")
print()

print(len(s))

#구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} x {j} = {i*j}")