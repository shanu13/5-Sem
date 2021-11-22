from typing import List, Dict, Set
from doctest import testmod
from collections import Counter
from random import randint
from functools import reduce


#PROBLEM 1
def strToList(string: str) -> List[str]:
    """
    Take a string as a input and returns a list to characters using list()

    doctests:
    >>> strToList("hello")
    ['h', 'e', 'l', 'l', 'o']
    >>> strToList("world")
    ['w', 'o', 'r', 'l', 'd']

    """
    return list(string)


#PROBLEM 2
def listToStr(char_list: List[str]) -> str:
    """
    Take a list of strings and return a resulting string using join()

    Doctest:
    >>> listToStr(["h", "e", "l", "l", "o"])
    'hello'
    >>> listToStr(['w', 'o', 'r', 'l', 'd'])
    'world'
    """
    return "".join(char_list)


#PROBLEM 3
def randomList(n: int) -> List[int]:
    """
    Take a input size n and returns a list of random ints
    >>> randomList(0)
    []
    """
    return [randint(0, n) for _ in range(n)]


#PROBLEM 4
def sortList(nums: List[int]) -> List[int]:
    """
    Takes a list of int and returns them in reverse sorted order

    Doctests:
    >>> sortList([3, 6, 1, 100, -3, 0])
    [100, 6, 3, 1, 0, -3]
    >>> sortList([1, 2, 4, 6])
    [6, 4, 2, 1]
    """
    return sorted(nums, reverse=True)


#PROBLEM 5
def frequency(nums: List[int]) -> Dict[int, int]:
    """
    Counts the frequency of occurance of elements in the list and return in the dictionary with element being the key

    Doctests:
    >>> frequency([1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3])
    {1: 6, 2: 9, 3: 8}
    >>> frequency([1,2,3,1,2,3,1,2,3])
    {1: 3, 2: 3, 3: 3}
    """
    return dict(Counter(nums))


#PROBLEM 6
def listToSet(nums: List[int]) -> Set[int]:
    """
    Take a list of int and returns all the unique elements present in the list

    Doctests:
    >>> listToSet([1,1,1,2,3,4])
    {1, 2, 3, 4}
    >>> listToSet([6, 7, 8, 9, 1, 6, 7])
    {1, 6, 7, 8, 9}
    """
    return set(nums)


#PROBLEM 7
def firstRepeating(nums: List):
    """
    Takes a list of items and returns the first repeating element

    >>> firstRepeating([1, 2, 3, 4, 2])
    2
    >>> firstRepeating(["a", "b", "a"])
    'a'
    """
    test = set()
    for val in nums:
        if val not in test:
            test.add(val)
        else:
            return val
    return None


#PROBLEM 8
def squaresAndCubes(n: int) -> Dict[int, List[int]]:
    """
    Returns a dictionary with a list of squares and cubes

    Doctests:
    >>> squaresAndCubes(4)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64]}
    >>> squaresAndCubes(0)
    {0: [0, 0]}
    >>> squaresAndCubes(-1)
    {}
    """
    return {i: [i ** 2, i ** 3] for i in range(n + 1)}


#PROBLEM 9
def zipItems(l1: List, l2: List) -> List:
    """
    Takes two lists of same length and returns zipping them together as one new list

    Doctests:
    >>> zipItems([1, 2, 3], [4, 5, 6])
    [(1, 4), (2, 5), (3, 6)]
    >>> zipItems(["hello"], ["world"])
    [('hello', 'world')]
    """
    return list(zip(l1, l2))


#PROBLEM 10
def listSquares(num: int) -> List[int]:
    """
    Take a int num and returns a list of squares from 0, 1, 2, ..., num

    Doctests:
    >>> listSquares(-1)
    []
    >>> listSquares(4)
    [0, 1, 4, 9, 16]
    """
    return [x * x for x in range(num + 1)]


#PROBLEM 11
def dictSquares(num: int) -> Dict[int, int]:
    """
    Take a num as input and returns squares from 0, 1, 2, ..., num

    >>> dictSquares(-1)
    {}
    >>> dictSquares(4)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    """
    return {x: x * x for x in range(num + 1)}


#PROBLEM 12
def intSquares(val: int) -> int:
    """
    Return the square of given number
    """
    return val * val


class CopyAndApply:

    def __init__(self, nums: List[int]) -> None:
        """Saves a copy of nums in a local variable"""
        self.nums = nums[:]

    def apply(self, func) -> List:
        """
        Applies the function to the list and returns the values

        Doctests:
        >>> l = CopyAndApply([1,2,3,4])
        >>> print(l.apply(intSquares))
        [1, 4, 9, 16]
        >>> print(l.apply(lambda x: x * x))
        [1, 4, 9, 16]
        >>> a = CopyAndApply(["a", "b"])
        >>> a.apply(intSquares)
        Function intSquares is not callable on the <class 'str'> type
        """
        try:
            return list(map(func, self.nums))
        except TypeError:
            print(f"Function {func.__name__} is not callable on the {type(self.nums[0]) if self.nums else None} type")


#PROBLEM 13
def mapUpper(string: List[str]) -> List[str]:
    """
    Takes a list of strings and return in all caps

    >>> mapUpper(["hello", "world"])
    ['HELLO', 'WORLD']
    >>> mapUpper([])
    []
    """
    return list(map(str.upper, string))


#PROBLEM 14
def product(nums: List[int]) -> List[int]:
    """
    Take a list of integers and return the product of all its elements

    >>> product([1, 2, 3, 4, 5])
    120
    >>> product([0, 23, 4, 2, 9])
    0
    """
    return reduce(lambda x, y: x * y, nums)


if __name__ == "__main__":
    testmod()
