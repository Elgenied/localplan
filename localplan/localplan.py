"""Main module."""
import random
import string

def generate_random_string(length=10, upper=False, digits=False, punctuation=False):
    """generate_random_string

    Args:
        length (int, optional): _description_. Defaults to 10.
        upper (bool, optional): _description_. Defaults to False.
        digits (bool, optional): _description_. Defaults to False.
        punctuation (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """    
    letters = string.ascii_lowercase
    if upper:
        letters += string.ascii_uppercase
    if digits:
        letters += string.digits
    if punctuation:
        letters += string.punctuation
    
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_lucky_number(length=1):
    """_generate_lucky_number

    Args:
        length (int, optional): _description_. Defaults to 1.

    Returns:
        _str_: rerurns a string of length 1
    """    
    result_str = ''.join(random.choice(string.digits) for i in range(length))
    return result_str