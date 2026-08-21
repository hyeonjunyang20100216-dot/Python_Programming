a = "Python"
print(a,type(a))
b = 'python'
print(b,type(b))


print(" I'll be back")
print('I\'ll be back')

multiline = """
Life is short
You need Python
"""
print(multiline)


def func():
    """이 함수는 아무것도 하지 않습니다."""
    pass

print(func.__doc__)

#문자열 연결
print("Hello" + "World")

#문자열 반복
print("Hello" * 10)
print("-"*100)

print("Hello"+10)