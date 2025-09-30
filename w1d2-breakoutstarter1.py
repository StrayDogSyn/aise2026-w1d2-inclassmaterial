from typing import List, Dict, TextIO
import io

# 1. Truthy & Falsy
def has_items(lst: List[int]) -> bool:
    """
    Return True if the input list contains one or more items, otherwise False.

    Args:
        lst: A list of integers.

    Returns:
        True if the list length is greater than zero, else False.
    """
    return bool(lst)


# 2. Ternary Operator
def absolute_value(n: int) -> int:
    """
    Return the absolute value of the integer n using ternary operator.

    Args:
        n: An integer.

    Returns:
        The non-negative magnitude of n.
    """
    return n if n >= 0 else -n


# 3. Walrus
def read_non_empty_lines(file: TextIO) -> None:
    """
    Print each non-empty, non-comment line from a file-like object. 
    
    # The readline() method reads the next line from the file each time it is called, 
    # returning an empty string when the end of the file is reached.

    Args:
        file: A text file-like object supporting .readline().

    Returns:
        None. Lines that are not blank and not starting with '#' are printed.
    """
    while (line := file.readline()) != "":
        if line.strip() != "" and not line.startswith("#"):
            print(line.rstrip("\n"))


# 4. Match Case
def day_name(num: int) -> str:
    """
    Map a 1–7 integer to the corresponding weekday name using match/case.

    Args:
        num: Integer day number where 1=Monday and 7=Sunday.

    Returns:
        The weekday name for 1–7, otherwise "Invalid".
    """
    match num:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid"


if __name__ == "__main__":
    print(has_items([]))
    print(has_items([1, 2]))
    # Expected:
    # False
    # True

    print(absolute_value(-3))
    print(absolute_value(5))
    # Expected:
    # 3
    # 5

    sample = io.StringIO(
        "# comment\n"
        "\n"
        "alpha\n"
        "  \n"
        "# another\n"
        "beta\n"
    )
    read_non_empty_lines(sample)
    # Expected:
    # alpha
    # beta

    print(day_name(1))
    print(day_name(7))
    print(day_name(9))
    # Expected:
    # Monday
    # Sunday
    # Invalid
