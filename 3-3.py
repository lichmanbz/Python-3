from typing import Any, Dict, List, Union

def function_name(search: str, status: bool, *args: Union[int, str], **kwargs: Dict[str, Any]) -> Union[List[int], str]:

    Union[List[int], str]: 
        - Если search 
    
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
