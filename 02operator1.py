x = 2
y = 4
z = 8

print("x + y", x + y)
print("x - y", x - y)
print("x * y", x * y)
# 나누기 연산. 결과는 실수(float)형으로 반환
print("x / y", x / y)
# 나누기 연산. 결과는 정수형 반환(몫)
print("x // y", x // y)
# 거듭제곱. x의 y승의 결과 반환
print("x ** y", x ** y)
# 파이썬에서 제공하는 기본함수로 y제곱의 결과 반환
print("pow(x, y)", pow(x, y))
# x의 y승의 결과를 z로 나눈 나머지가 반환
print("pow(x, y, z)", pow(x, y, z))
# x를 y로 나눈 몫과 나머지를 Tuple(튜플)로 반환한다.
print("divmod(x, y)", divmod(x, y))

""" 
수학관련 여러가지 함수를 가지고 있는 math 모듈을 현재 문서에 import 한 후
팩토리얼 함수를 실행
"""

import math
print("math.factorial(5)", math.factorial(5))