from sympy import div


def addition(a,b):
    c = a + b
    print(f'Addition of {a} and {b} == {c} ')
    return c

def multiplication(a,b):
    mul = a * b
    print(f'Multiplication of {a} and {b} == {mul} ')
    return mul

def division(a,b):
    div = a/b
    print(f'Division of {a} and {b} == {div} ')
    return div

if __name__ == "__main__":
    addition(11,22)
    multiplication(4,8)
    division(55,5)
