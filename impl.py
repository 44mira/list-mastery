from typing import Callable

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

def reverse(xs : list[any]) -> list[any]:
    """ 
    Reverse a list

    :param xs: list to be reversed
    :return:   the reversed list
    """
    for i in range(len(xs)//2):
        xs[i], xs[len(xs)-i-1] = xs[len(xs)-i-1], xs[i]
    return xs

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


print(partition([1,2,3,4,5], [0,0,0,0,0]))


