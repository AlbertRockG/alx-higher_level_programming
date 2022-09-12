#!/usr/bin/python3
# 4-list_division.py
# AlbertG <rafgangbadja@gmail.com>

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    Args:
        my_list_1 (list): The list of divisors.
        my_list_2 (list): The list of dividends.
        list_length (int): The length of the new list.

    Returns:
        A list of quotients.
    """

    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
