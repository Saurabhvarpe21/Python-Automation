
def addition1(a,b):
    add = a+b
    print(f'Addition of {a}, {b} is {add}')
    return add

def multiplication(a,b):
    mul = a*b
    print(f'Multiplication of {a}, {b} is {mul} ' )
    return mul

print('__name__ is :', __name__)
if __name__ == 'calculation':
    addition1(11,22)
    multiplication(4,8)