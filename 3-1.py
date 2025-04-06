from typing import List

def multiply_elements(elements: List[int], multiplier: int = 2) -> List[int]:
    """Умножает каждый элемент списка на заданный множитель.
    
    Args:
        elements (List[int]): Список чисел для умножения.
        multiplier (int): Число, на которое нужно умножить элементы. По умолчанию 2.
    
    Returns:
        List[int]: Новый список с умноженными элементами.
    """
    return [x * multiplier for x in elements]

def multiply_with_lambda(elements: List[int], multiplier: int = 2) -> List[int]:
    """Умножает каждый элемент списка на заданный множитель, используя лямбда-функцию.
    
    Args:
        elements (List[int]): Список чисел для умножения.
        multiplier (int): Число, на которое нужно умножить элементы. По умолчанию 2.
    
    Returns:
        List[int]: Новый список с умноженными элементами.
    """
    return list(map(lambda x: x * multiplier, elements))

def main():
    input_numbers = input("Введите список чисел через пробел: ")
    numbers = list(map(int, input_numbers.split()))
    
    multiplier_input = input("Введите множитель (по умолчанию 2): ")
    multiplier = int(multiplier_input) if multiplier_input else 2
    
    result_function = multiply_elements(numbers, multiplier)
    result_lambda = multiply_with_lambda(numbers, multiplier)
    
    print(f"Результат (функция): {result_function}")
    print(f"Результат (лямбда-функция): {result_lambda}")

if __name__ == "__main__":
    main()
