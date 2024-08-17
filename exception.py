
import sys

try:
    x=int(input("give the first num x: "))
    y=int(input("give the secon num y: "))
except ValueError:
    print('Please input valied number')
    sys.exit(1)
try:
    result=x/y
    print(result)
except ZeroDivisionError:
    print('you can not divide by zero')
    sys.exis(1)