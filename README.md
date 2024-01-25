# List Mastery

> All of the code will be in Python and will be implemented in a way that prioritizes simplicity over efficiency.
> **Again, these are not necessarily the optimal way to implement these functions.**

## Table of Contents
- [Length](README.md#Length)
- [Shape](README.md#Shape)
- [Rank/Depth](README.md#RankDepth)
- [Take](README.md#Take)
- [Drop](#Drop)
- [Range](#Range)
- [Reverse](#Reverse)
- [Sort](#Sort)
- [Nub/Deduplicate](#Nub/Deduplicate)
- [Map](#Map)
- [IndexOf](#IndexOf)
- [Fold/Reduce](#FoldReduce)
- [Scan](#Scan)
- [Zip/Couple/Stitch](#ZipCoupleStitch)
- [Keep/Replicate](#KeepReplicate)
- [Filter](#Filter)
- [Window/Roll](#WindowRoll)
- [Table](#Table)
- [Group](#Group)
- [Partition](#Partition)

## Length
```python
def length(xs : list[any]) -> int:
    """ 
    Get the length of a list

    :param xs: the list to get the length of
    :return:   the length of the list
    """
    count = 0
    for _ in xs: count += 1
    return count
```
- Python has a built-in `len` function.

## Shape
- Most high-level languages do not put a restriction on shape, hence a proper implementation would be not practical.

## Rank/Depth
```python
def rank(xs : any) -> int:
    """ 
    Returns the rank of a list, checking the first element recursively

    :param xs: the element to be checked.
    :return:   the rank of the list
    """
    if isinstance(xs, list): return 1 + rank(xs[0] if xs else 0)
    else : return 0
```
- This code only checks the first element, leading to incorrect results on uneven shapes.

## Take
```python
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
```
- Some implementations allow for negative `n`, taking from the end instead.
- In Python, the same effect can be done using `slices`.
```python
[1,2,3,4,5][:2] == [1,2]
```
## Drop
```python
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
```
- Some implementations allow for negative `n`, dropping from the end instead.
- In Python, the same effect can be done using `slices`.
```python
[1,2,3,4,5][2:] == [3,4,5]
```
## Range
```python
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
```
- Python has a built-in `range` function that utilizes a generator.

## Reverse
```python
def reverse(xs : list[any]) -> list[any]:
    """ 
    Reverse a list

    :param xs: list to be reversed
    :return:   the reversed list
    """
    for i in range(len(xs)//2):
        xs[i], xs[len(xs)-i-1] = xs[len(xs)-i-1], xs[i]
    return xs
```
- Python has a built-in `reversed` function that utilizes a generator.
	- The same effect can also be achieved by doing a negative `step` slice. 
```python
list(reversed([1,2,3,4,5])) == [1,2,3,4,5][::-1]
```

## Sort
```python
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
```
- This is *Bubble sort*, an $O(n^2)$ implementation. Most built-in functions such as Python's `sorted` use a faster $O(n \log n)$ implementation.
- Most built-in sorts let you define a *comparison function.*

## Nub/Deduplicate
```python
def nub(xs : list[any]) -> list[any]:
    """ 
    Removes the duplicates in a list, preserving order

    :param xs: the list to be deduplicated
    :return:   the list with unique elements
    """
    seen = set()    # the seen.add() will always return None, the `or` branch is simply there to execute the add.
    return [x for x in xs if not (x in seen or seen.add(x))] 
```
- A lot of `dedup` algorithms involve piping your list into a `hashset`, but you have to be careful as most hashsets are unordered.

## Map
```python
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
```
- Python has a built-in `map` function that uses generators.
	- The same behavior can also be trivially implemented using list comprehensions.
```python
[x*2 for x in [1,2,3]] == [2,4,6]
```
- The mapping function has to be a *unary/monadic* function.
- Mapping function does not necessarily have to be a *monoid* over the type.
	- This means it can return types that differ from the input.
- A special case of `map` is `select`, wherein the input list is treated as a mask of indices to be gotten from a second list.
```python
def select(xs : list[int], ys : list[any]) -> list[any]:
    return map(xs, lambda x: ys[x])
```

## IndexOf
```python
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
```
- Often times used with `map` in the form:  `map(lambda e: indexof(xs, e), input_mask)`.

## Fold/Reduce
```python
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

```
- Python has a built-in `reduce` function found in the `functools` package.
- The reducing function has to be a *binary/dyadic* function, one of the arguments being the accumulator.
- Most recursive algorithms can be implemented as a reduce/fold.
- Folds can either be from the left (head recursive), or the right (tail recursive).

## Scan
```python
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
```
- Python has a built-in scan function, called `accumulate` found in the `itertools` package.
	- This implementation uses generators.
- The reducing function has to be a *binary/dyadic* function, one of the arguments being the accumulator.
- Scans can either be from the left (head recursive), or the right (tail recursive).

## Zip/Couple/Stitch
```python
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
```
- Python has a built-in `zip` function.
- Some implementations use lists to represent pairs instead of tuples.
- A common combination that is used is *zip_with*, zipping pairs and then mapping a function in one pass.
```python
def zip_with(xs : list[any], ys: list[any], f : Callable[[(any,any)], any]) -> list[(any,any)]:
    res = []
    for i in range(min(len(xs), len(ys))): res.append(f(xs[i], ys[i]))
    return res
```

## Keep/Replicate
```python
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
```
- `keep` is how most array languages achieve the behavior of `filter`.
- Some implementations of `keep` require matching shapes of the input list and the mask.
	- Most implementations of `keep` do not strictly require the use of boolean masks, and is why it is sometimes called as `replicate`.
```python
def replicate(xs : list[any], mask : list[int]) -> list[any]:
    res = []
    for i, x in enumerate(xs): res.extend([x] * mask[i])   # keep n copies of the element based on the mask
    return res
```
- An input of `replicate([1,2,3,4], [0,2,4,1])` would yield an output of `[2,2,3,3,3,3,4]`.

## Filter
```python
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
```
- Python has a built-in `filter` function that uses generators.
	- The same behavior can also be implemented trivially using list comprehensions.
```python
[x for x in [1,2,3,4,5] if x % 2 == 0] == [2,4]
```
- `filter` can be implemented using a combination of `map` and `keep`.
	- This is the approach array languages take.
```python
def _filter(xs : list[any], f: Callable[[any], bool]) -> list[any]:
    return keep(xs, map(xs, f))
```

## Window/Roll
```python
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
```
- A special-case of `window` is Python's `pairwise` found in the `itertools` package, which is a *2-wise* or *adjacent* window.
	- This implementation uses generators.

## Table
```python
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
```
- The same behavior can be trivially implemented with Python comprehensions
```python
table(xs, ys, f) == [f(x,y) for x in xs for y in ys]
```
- Python has a built-in `product` in found in the `itertools` package, which does the cartesian product part of table.
	- Therefore, `table` can be written as a map over `product`.
```python
def _table(xs : list[any], ys : list[any], f : Callable[[any, any], any]):
    return map(lambda t : f(t[0],t[1]), product(xs, ys))
```

## Group
```

## Group
```python
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
```
- Some implementations of `group` (like Uiua) allow for a mapping function.

## Partition
```python
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
```
- Some implementations of `partition` (like Uiua) allow for a mapping/reducing function.
- `partition` is most commonly used in parsing.
	- A special-case abstraction of `partition` being `split`.
