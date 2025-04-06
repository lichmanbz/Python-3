from typing import Any, Dict, List, Union

def function_name(search: str, status: bool, *args: Union[int, str], **kwargs: Dict[str, Any]) -> Union[List[int], str]:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Параметры:
    search (str): Определяет, какая часть аргументов будет обработана ('args' или 'kwargs').
    status (bool): Определяет, как обрабатываются аргументы (истинное значение для фильтрации целых чисел).
    *args (Union[int, str]): Неименованные аргументы, которые могут быть либо целыми числами, либо строками.
    **kwargs (Dict[str, Any]): Именованные аргументы в виде пар "ключ-значение".

    Возвращает:
    Union[List[int], str]: 
        - Если search == "args" и status == True: Возвращает список целых чисел из args.
        - Если search == "args" и status == False: Возвращает строку, составленную из args.
        - Если search == "kwargs": Возвращает строку с ключами и значениями из kwargs.
    
    Исключения:
    ValueError: Если значение search не равно 'args' или 'kwargs'.
    """
    
    result: List[int] = []
    result_2: str = ""
    
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")
