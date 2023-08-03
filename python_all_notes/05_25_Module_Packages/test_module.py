def my_fun(string):
    return f'This is your string : {string}'

def add(a,b):
    return a+b

print('Value of __name__ is >> ', __name__)

if __name__ == "test":
    
    print(my_fun('Data Science'))
    obj = add(12,7)
    print(obj)