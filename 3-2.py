import math

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть int или float.")
    return a + b

def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть int или float.")
    return a - b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть int или float.")
    return a * b

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть int или float.")
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return a / b

def power(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть int или float.")
    return a ** b

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом.")
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён.")
    return math.factorial(n)

def sine(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Аргумент должен быть int или float.")
    return math.sin(x)

def median(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Аргумент должен быть списком.")
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("Все элементы списка должны быть int или float.")
    return sorted(numbers)[len(numbers) // 2]

def main():
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал")
    print("7. Синус")
    print("8. Медиана")
    print("--------------------")
    
    while True:
        operation = input("Операция (или 'exit' для выхода): ")
        if operation.lower() == 'exit':
            break
        
        try:
            if operation == '1':
                a = float(input("Слагаемое 1: "))
                b = float(input("Слагаемое 2: "))
                print(">>>", add(a, b))
                
            elif operation == '2':
                a = float(input("Уменьшаемое: "))
                b = float(input("Вычитаемое: "))
                print(">>>", subtract(a, b))
                
            elif operation == '3':
                a = float(input("Множитель 1: "))
                b = float(input("Множитель 2: "))
                print(">>>", multiply(a, b))
                
            elif operation == '4':
                a = float(input("Делимое: "))
                b = float(input("Делитель: "))
                print(">>>", divide(a, b))
                
            elif operation == '5':
                a = float(input("Основание: "))
                b = float(input("Степень: "))
                print(">>>", power(a, b))
                
            elif operation == '6':
                n = int(input("Введите число для факториала: "))
                print(">>>", factorial(n))
                
            elif operation == '7':
                x = float(input("Введите угол в радианах: "))
                print(">>>", sine(x))
                
            elif operation == '8':
                nums = list(map(float, input("Список чисел (через пробел): ").split()))
                print(">>>", median(nums))
                
            else:
                print("Некорректная операция, попробуйте еще раз.")
                
        except (TypeError, ValueError, ZeroDivisionError) as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
