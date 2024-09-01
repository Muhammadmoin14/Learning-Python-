#               ------ TYPES DEFINITIONS IN PYTHON ------

from typing import List, Tuple, Dict, Union 

#? 1. Variable Type
n : int = 10;
print(n);

#? 2. Function Type

def add(a: int, b: int) -> int:
    return a + b;

result = add(5 , 3);
print(result);

#? 3. List of integers 

numbers: List[int] = [1, 2, 3, 4, 5] 

#? 4. Tuple of a string and an integer 

person: Tuple[str, int] = ("Alice", 30) 

#? 5. Dictionary with string keys and integer values 

scores: Dict[str, int] = {"Alice": 90, "Bob": 85} 

#? 6. Union type for variables that can hold multiple types 

identifier: Union[int, str] = "ID123" 
identifier = 12345  # Also valid      