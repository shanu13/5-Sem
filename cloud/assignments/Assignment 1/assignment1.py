from functools import reduce
from typing import Dict, List, Set
import random
import doctest

#1
def StringToList(word: str) -> List[str]: 
    """Return the List of Characters from by word
    doctests:
    >>> StringToList("Python")
    ['P', 'y', 't', 'h', 'o', 'n']
    >>> StringToList("Java")
    ['J', 'a', 'v', 'a']
    """
    char_list = list(word)
    return char_list

#2
def ListToString(wordList : List[str]) -> str:
    """Return the string by joining the list charcters

    doctest:
    >>> ListToString(['P', 'y', 't', 'h', 'o', 'n'])
    'Python'
    >>> ListToString(['J', 'a', 'v', 'a'])
    'Java'

    """
    return "".join(wordList)

# 3
def randomGenerate(n : int) -> List[int]:
    """ Generate n Random Numbers List
    doctest :
    >>> randomGenerate(0)
    []
    """
    rnd_list = [random.randint(0,n) for _ in range(n)]
    return rnd_list

# 4
def SortDescending(numList : List[int]) -> List[int] :
    """Return the list sorted in desending order 

    doctest:
    >>> SortDescending([1, 5, 0, 3, 2 ])
    [5, 3, 2, 1, 0]
    >>> SortDescending([10, 80, 65, 40, 33 ])
    [80, 65, 40, 33, 10]

    """
    sortList = sorted(numList,reverse=True)
    return sortList

# 5
def GetFrequency(nums : List[int]) -> Dict:

    """Returns the frequency of each number in the list num.

    doctests:
    >>> GetFrequency([1, 1, 3, 2, 3, 2, 3, 2, 2,3,3,3,2])
    {1: 2, 3: 6, 2: 5}
    >>> GetFrequency([1, 4, 5, 5, 2, 3, 2, 4, 6])
    {1: 1, 4: 2, 5: 2, 2: 2, 3: 1, 6: 1}


    """

    frequency = {}
    for i in range(len(nums)):
        key = nums[i];
        value = nums.count(key)
        frequency.update({key:value})

    return frequency    

# 6
def UniqueNums(nums : List[int]) -> Set[int] :
    """Returns the unique element from the given list numList.

    doctests:
    >>> UniqueNums([1, 1, 3, 2, 3, 2, 3, 2, 2])
    {1, 2, 3}
    >>> UniqueNums([1, 4, 4, 2, 3, 3, 2, 1, 6])
    {1, 2, 3, 4, 6}
    """

    return  set(nums) 

# 7
def CheckRepeating(nums : List[int]) :
    """Return the first element which is repeating in list
    doctest:
    
    >>> CheckRepeating([1,2,5,8,5,1])
    5
    >>> CheckRepeating([1,2,1])
    1
    """

    s = set()
    for i in range(len(nums)):
        if nums[i] not in s:
            s.add(nums[i])
        else :
             return nums[i]

    return None 

# 8
def SqAndCube(num : int) -> dict[int,List[int]]  :
    """Returns a dictionary containing keys from 0 to n with the square and cube mapped.

    doctests:
    >>> SqAndCube(3)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27]}
    >>> SqAndCube(5)
    {0: [0, 0], 1: [1, 1], 2: [4, 8], 3: [9, 27], 4: [16, 64], 5: [25, 125]}
    """
    res = {}
    for i in range(num+1):
        value = [i**2,i**3]
        res.update({i:value})

    return res    

# 9
def MakeTuple(list1 : List, list2 : List ) -> List :
    """
    Takes two lists of same length and returns zipping them together as one new list

    Doctests:
    >>> MakeTuple([1, 2, 3], [4, 5, 6])
    [(1, 4), (2, 5), (3, 6)]
    >>> MakeTuple(["hello"], ["world"])
    [('hello', 'world')]
    """

    res = list(zip(list1,list2))
    return res

# 10
def generateSqList(num: int) -> List[int]: 
    """Returns a list of squares from 0 to num using list comprehension.
    >>> generateSqList(5)
    [0, 1, 4, 9, 16, 25]
    >>> generateSqList(10)
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    newList = [x ** 2 for x in range(num + 1)]
    return newList

# 11
def generateSqDict(num: int) -> List[int]:  # Problem 11
    """Returns a dictionary  mapping squares from 0 to n using dictionary comprehension.
    >>> generateSqDict(5)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    >>> generateSqDict(10)
    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
    """
    newDict = {x: x ** 2 for x in range(num + 1)}
    return newDict

# 12
class MyClass :

    def __init__(self,nums : List):
        self.list = nums[:] 

    def apply(self,func)  :
        try : 
            return map(func,self.list)   

        except TypeError:
            print("Type error or invalid Operations")



# 13
def toUpper(nums : List[str]) -> List[str] :
    """Returns a list of words that has been uppercased from an existing list wordList using 'functools.map'.
    >>> toUpper(['aa', 'bb', 'cd', 'e'])
    ['AA', 'BB', 'CD', 'E']
    >>> toUpper(['word', 'is', 'upper', 'case'])
    ['WORD', 'IS', 'UPPER', 'CASE']
    """

    newList = map(str.upper,nums)
    return list(newList)

# 14
def toReduce(nums : List[int]) -> int :

    """Returns the product of all the numbers in the list numList using 'functools.reduce'.
    >>> toReduce([1, 2, 3, 4, 5])
    120
    """
    res = reduce(lambda a,b : a*b , nums)
    return res


if __name__== "__main__":
    doctest.testmod()
