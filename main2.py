def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f'We have problems {exc}')
        else:
            print(f'Result - {result}')
    return checker

@checker
def calculate(expression):
    return eval(expression)

@checker
def division(number, div):
    return number / div

# checker(calculate, '2+2')

# calculate =  checker(calculate)

calculate('3+2')
division(2, 1)
