# Документація до коду Python

Цей документ пояснює, як працює декоратор `checker`, який обробляє виключення та виводить результат роботи функцій.

## Опис

1. **Декоратор `checker`:**
   - Це декоратор, який приймає функцію і обробляє виключення.
   - Якщо функція викликається без помилок, результат її роботи виводиться.
   - Якщо виникає помилка, виводиться повідомлення про помилку.

2. **Функція `calculate`:**
   - Приймає математичний вираз у вигляді рядка та обчислює його за допомогою `eval`.
   - Працює тільки з правильними виразами, інакше виникне помилка.

3. **Функція `division`:**
   - Приймає два числа і обчислює їхнє ділення.
   - Виводить помилку, якщо друге число дорівнює нулю (ділення на нуль).

## Приклад використання

### Код:

```python
def checker(function):
    def wrapper(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f'We have problems: {exc}')
        else:
            print(f'Result: {result}')
    return wrapper

@checker
def calculate(expression):
    return eval(expression)

@checker
def division(number, div):
    return number / div

# Виклики функцій
calculate('3+2')  # Результат: 5
division(2, 1)    # Результат: 2.0
