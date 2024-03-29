from typing import Callable
from itertools import product

def length(xs : list[any]) -> int:
    """ 
    Get the length of a list

    :param xs: the list to get the length of
    :return:   the length of the list
    """
    count = 0
    for _ in xs: count += 1
    return count

def range(n : int) -> list[int]:
	"""
	Generate numbers 0 to n-1

	:param n: upper bound exclusive
	:return:  the resulting list
	"""
	res, count = [], 0
	while count < n:
		res.append(count)
		count += 1
	return res

def concat(xs : list[any], ys : list[any]) -> list[any]:
    """
    Joins two lists together

    :param xs: list 1
    :param ys: list to be joined at the end
    :return:   both lists joined together
    """
    for y in ys: xs.append(y)
    return xs

def deshape(xs : list[list[any]]) -> list[any]:
    """
    Returns all of the elements of a matrix.

    :param xs: list to be flattened
    :return:   flattened list
    """
    res = []
    for row in xs:
        for x in row: res.append(x)
    return res

def reverse(xs : list[any]) -> list[any]:
    """ 
    Reverse a list

    :param xs: list to be reversed
    :return:   the reversed list
    """
    for i in range(len(xs)//2):
        xs[i], xs[len(xs)-i-1] = xs[len(xs)-i-1], xs[i]
    return xs

def rotate(xs : list[any], n : int) -> list[any]:
    """ 
    Rotates an array xs to the left by n
    A negative n makes it rotate to the right instead.

    :param xs: the list to be rotated 
    :param n:  steps to rotate
    :return:   rotated list
    """
    n %= len(xs)    # rotating at the length of xs goes back to initial state
    res = xs[n:]        # drop n
    res.extend(xs[:n])  # take n
    return res

def transpose(xs : list[list[any]]) -> list[list[any]]:
    """ 
    Transposes a list that is at least rank 2, swapping its top 2 ranks.
    On matrices this would be swapping rows with columns.

    :param xs: the matrix to be transposed
    :return:   the transposed matrix
    """
    res = [[0] * len(xs) for _ in range(len(xs[0]))]   # initialize resulting matrix

    for i in range(len(xs)):
        for j in range(len(xs[0])):
            res[j][i] = xs[i][j]
    return res

def sort(xs : list[any]) -> list[any]:
    """ 
    Sorts a list in ascending order

    :param xs: list to be sorted
    :return:   the sorted list
    """
    for i in range(len(xs)-1):
        for j in range(len(xs)-1-i):
             if xs[j]>xs[j+1]:
                xs[j], xs[j+1] = xs[j+1], xs[j]
    return xs

def nub(xs : list[any]) -> list[any]:
    """ 
    Removes the duplicates in a list, preserving order

    :param xs: the list to be deduplicated
    :return:   the list with unique elements
    """
    seen = set()    # the seen.add() will always return None, the `or` branch is simply there to execute the add.
    return [x for x in xs if not (x in seen or seen.add(x))] 

def rank(xs : any) -> int:
    """ 
    Returns the rank of a list, checking the first element recursively

    :param xs: the element to be checked.
    :return:   the rank of the list
    """
    if isinstance(xs, list): return 1 + rank(xs[0] if xs else 0)
    else : return 0

def take(xs : list[any], n : int) -> list[any]:
    """  
    Takes the first n elements of a list

    :param xs: the list to be taken from
    :param n:  the number of elements to be taken
    :return:   the elements taken
    """
    res, counter = [], 0
    while counter < n:
        res.append(xs[counter])
        counter += 1
    return res

def drop(xs : list[any], n : int) -> list[any]:
    """ 
    Drops the first n elements of a list

    :param xs: the list to be dropped from
    :param n:  the number of elements to drop
    :return:   the elements left
    """
    while n:
        xs.pop(0)
        n -= 1
    return xs

def map(xs : list[any], f : Callable[[any], any]) -> list[any]:
    """ 
    Maps a function f on to a list

    :param xs: the list to be mapped over
    :param f:  the mapping function
    :return:   the mapped list
    """
    res = [] 
    for x in xs: res.append(f(x))
    return res

def select(xs : list[int], ys : list[any]) -> list[any]:
    return map(xs, lambda x: ys[x])

def indexof(xs : list[any], target : any) -> int:
    """
    Return the index of an item from a list, returns the size length + 1 when not found

    :param xs:     the list to be searched
    :param target: the item to be searched for
    :return:       index of the searched item or length + 1 when not found
    """
    for i, x in enumerate(xs):
        if target == x: return i
    return len(xs)

def reduce(xs : list[any], f : Callable[[any, any], any], a : any = None) -> any:
    """ 
    Reduces a list's rank using an accumulating function

    :param xs: the list to be reduced
    :param f:  the reducing function
    :param a:  [optional] the starting accumulator
    :return:   the result of the reduction
    """
    if a == None:
        a = xs[0]
        xs.pop(0)   # remove duplicate first
    for x in xs: a = f(x, a)
    return a

def scan(xs : list[any], f : Callable[[any,any], any], a : any = None) -> any:
    """  
    Reduces a list's rank using an accumulating function, while keeping track of intermediary values

    :param xs: the list to be reduced
    :param f:  the reducing function
    :param a:  [optional] the starting accumulator
    :return:   the result of the scan
    """
    if a == None:
        a = xs[0]
        xs.pop(0)   # remove duplicate first
    res = [a]
    for x in xs:
        a = f(x, a)
        res.append(a)
    return res

def zip(xs : list[any], ys: list[any]) -> list[(any,any)]:
    """      
    Zips together two lists, truncating on the shorter one

    :param xs: list 1
    :param ys: list 2
    :return:   list of zipped pairs
    """
    res = []
    for i in range(min(len(xs), len(ys))): res.append((xs[i], ys[i]))
    return res

def zip_with(xs : list[any], ys: list[any], f : Callable[[(any,any)], any]) -> list[(any,any)]:
    res = []
    for i in range(min(len(xs), len(ys))): res.append(f(xs[i], ys[i]))
    return res

def keep(xs : list[any], mask : list[bool]) -> list[any]:
    """  
    Keeps elements from a list based on a boolean mask

    :param xs:   list to be kept from
    :param mask: mask used for determining which elements to keep, must be greater than or equal to length of xs
    :return:     the kept values
    """
    res = []
    for i, x in enumerate(xs): 
        if mask[i]: res.append(x)
    return res
    
def replicate(xs : list[any], mask : list[int]) -> list[any]:
    res = []
    for i, x in enumerate(xs): res.extend([x] * mask[i])   # keep n copies of the element based on the mask
    return res

def filter(xs : list[any], f : Callable[[any], bool]) -> list[any]:
    """
    Filters a list based on a predicate f

    :param xs: list to be filtered
    :param f:  the filtering predicate
    :return:   the filtered list
    """
    res = []
    for x in xs:
        if f(x): res.append(x)
    return res

def _filter(xs : list[any], f: Callable[[any], bool]) -> list[any]:
    return keep(xs, map(xs, f))

def window(xs : list[any], r : int) -> list[any]:
    """
    Return a rolling n-wise window of a list

    :param xs: the list to be windowed
    :param n:  the size of a window
    :return:   the n-wise windows
    """
    l, res = 0, []      # l is the left pointer
    while r <= len(xs):
        res.append(xs[l:r])
        l += 1
        r += 1
    return res

def table(xs : list[any], ys : list[any], f : Callable[[any, any], any]):
    """
    Takes two lists and performs a function f on all pairs of elements between
    Also known as cartesian product.
    
    :param xs: list 1
    :param ys: list 2
    :param f:  the binary function to be applied on element pairs
    :return:   the mapped cartesian product of the two lists
    """
    res = [[0] * len(ys) for _ in range(len(xs))]   # initialize the n * m matrix to be returned
                                                    # n and m being the lengths of xs and ys, respectively
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            res[i][j] = f(x, y)
    return res

def _table(xs : list[any], ys : list[any], f : Callable[[any, any], any]):
    return map(lambda t : f(t[0],t[1]), product(xs, ys))

def group(xs : list[any], mask : list[int]) -> list[list[any]]:
    """
    Groups elements based on a mask of keys

    :param xs:   the list to be grouped
    :param mask: the mask of keys
    :return:     the list of grouped lists
    """
    memo = {}
    for i, x in enumerate(xs):
        if mask[i] not in memo: memo[mask[i]] = []
        memo[mask[i]].append(x)
    return list(memo.values())

def partition(xs : list[any], mask : list[int]) -> list[list[any]]:
    """
    Partitions elements based on a mask of keys, omitting keys of <= 0

    :param xs:   the list to be partitioned
    :param mask: the mask of keys
    :return:     the list of partitioned lists
    """
    prev, res = 0, []
    curr = []
    for i, x in enumerate(xs):
        if mask[i] <= 0: 
            prev = 0
            continue
        elif mask[i] != prev:
            if curr: res.append(curr.copy())
            curr.clear()
        curr.append(x)
        prev = mask[i]
    if curr: res.append(curr)
    return res



