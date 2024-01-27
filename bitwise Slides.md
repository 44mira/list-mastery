---
theme: night
bg: black
---
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.css"> <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

## code instinct:
#### *List Mastery*

---

![[Pasted image 20240122030334.png]]

note: If there is anything that you will eventually find out about having a hobby, or a skill

---

![[Pasted image 20240122030358.png]]

note: It is that it is always better as a sport

---

competitive programming

note: Competitive programming, or as I would like to call it, Ranked programming, is a sport wherein people like me who like to code but don't have a job end up. 

---

![[Pasted image 20240122031022.png]]

note: I simply got sick of sitting in front of my computer and grinding out videogames such as League of Legends and Valorant. So instead I decided I would sit infront of my computer and grind out coding.

---

![[Pasted image 20240122031249.png]]

note: This is not me. Most of the time I refer to myself a competitive programming hobbyist, as it is quite difficult to land competitions here in Davao, and when I did get into one *ADDU's Hackathon*, I got absolutely obliterated.

---

![[Pasted image 20240122031545.png]]
Me:

note: By the way, this is me. I've only had one other speaking engagement, that being DEVCON's TechKwentuhan, wherein I did my talk "code poetry," a prequel to this talk that I am about to give tonight. 

---

<split even>
![[Pasted image 20240122032007.png|500x500]]
![[Pasted image 20240122032114.png|500x500]]
</split>

note: I am currently the Head of the Skill-Building Department of UP Mindanao SPARCS, which was "founded" by me and my two friends, Sharmaigne and Aaron. It was a "Fine, I'll do it myself" moment for the three of us as we really just wanted more focus on bridging the gap between beginners and professionals.

---

### \[\[ digression ]]

note: I'd like to think that the three of us are pretty active right now in various tech events in Davao, so if you come across us feel free to chat us up or just say hi! The three of us have experience with competitive programmning, Aaron does a lot of volunteer work, and Sharmaigne she's done 2 hosting events now.

---

![[Pasted image 20240122033842.png]]

note: Moreover, it was actually Sharmaigne who introduced me to competitive programming, and I still consider her to be much better at it than me. She comes up with the cleverest solutions, and most of the time I just help her write in a language. So yeah, if you see good code of mine, know that Sharmaigne probably helped with it.

---

### \[\[ end of digression ]]

---

<split gap="1">
<center>
![[Pasted image 20240122034255.png|500x275]]
![[Pasted image 20240122035050.png|500x275]]
</center>
</split>

note: So as you might be able to tell, I'm actually not *that* qualified to be giving this type of talk. I haven't actually participated in any competitions the past couple of months. 

---

CodeChef leaderboards:
<split even>
![[Pasted image 20240122035333.png]]
![[Pasted image 20240122035347.png]]
</split>
technically Country 12th if I was active

---

so what?

note: So what if I do competitive programming? And that's a valid question.

The answer: it is the best way to learn Data Structures and Algorithms, because you will *have* to use Data Structures and Algorithms. DSA is like the programmer's Calculus, most of them are afraid of it and don't know how to use them.

---

![[Pasted image 20240122040007.png]]

note: To put simply, competitive programming doesn't just train your ability to use data structures, it trains you to see patterns. To be able to code fast and produce efficient algorithms, you have to take advantage of these patterns. If you needed to sort an array of numbers, an algorithm that has been so well known and optimized by programmers way better than you, you shouldn't have to write your own anymore!

---

```python

def sort_nums(arr : list[int]) -> list[int]:
	arr.sort()       # built-in in-place sort
	return arr	


```

note: You'd do something the likes of this Python code. Not only is it terse, it's also optimized to run at O(n log n) time, which is the fastest a sort can go. Now if this was an exercise on implementing a sorting algorithm, then yes this beats the purpose. But if you were trying to pump out as many solved problems as you can in a competition, this saves you so much time, just because you knew how to use your language to manipulate your array.

---

#### Terminologies and Jargon:

note: Before we get into the meat of this talk, let's first define a few terms I might end up throwing around.

---

<h3 style="color: skyblue" >List</h3>

- most flexible data structure
- used for collections
- implemented as an *array* or a *linked list*

note: They are so flexible in fact that there are languages that have lists as the only data structure, called array languages.

---

| <span style="color: skyblue">term</span> | meaning                            |
| ---------------------------------------- | ---------------------------------- |
| Element / Atom                           | A singular member of a list        |
| Rank / Dimension / Axis                  | The level of nesting your list has |
| Row / Leading Axis                       | The elements at your highest rank  |
| Length                                   | The number of elements in the row  |
| Shape                                    | The length of every rank / axis    |

note: Note that for the Shape to make sense, all of the lengths in the same dimension must match.

---

#### Examples
```python
[[1, 2], [2, 3], [3, 4]] # Rank 2, Length 3, Shape [3, 2]
['a', 'b', 'c']          # Rank 1, Length 3, Shape [3]
4                        # Rank 0, Length 1, Shape []
```

```json
[
  [
    [1,2], 
    [2,3],
    [3,4]
  ],         
  [
    [3,4], 
    [4,5],
    [5,4]
  ]
]
```

note: A rank 2 list is also known as a matrix, a rank 1 also known as a vector, and a rank 0 also known as a scalar. Lets take a look at this JSON, Rank 3, Length 2, Shape \[2, 3, 2].

---

#### incase of information overload 

https://github.com/44mira/list-mastery

---

<h2><span style="color: #D26500">LIST MASTERY</span></h2>

note: and with all of that out of the way, we've finally reached the meat of the talk. List manipulation, and eventually, mastery. I'll go over common patterns in list manipulation, and how I would write them in 3 languages, Python, Elixir, and Uiua.

All of them will come with an example to demonstrate their usecase.

---

#### Length

Given an array `[1,2,3,4,5]`, return its length.

```python
len([1,2,3,4,5])    # python
```

 ```elixir
length [1,2,3,4,5]  # elixir
```

```elixir
length [1 2 3 4 5]   # uiua
```

---

#### Shape
Return the shape of  `xs`

```elixir
shape xs
```

---

#### Rank
Return the rank of `xs`

```elixir
length shape xs
```

---

#### Take
Return the first 5 elements of `xs`.

```python
xs[:5]
```

```elixir
Enum.take(xs, 5)
```

```elixir
take 5 xs
```

---

#### Drop
Return `xs` without the first 5 elements

```python
xs[5:]
```

```elixir
Enum.drop(xs, 5)
```

```elixir
drop 5 xs
```

---

#### Range
Return a list from `0` up to `n-1`

```python
list(range(n))
```

```elixir
Enum.to_list(0..n-1)
```

```elixir
range n
```

---

#### Reverse
Turn an ascending list `xs` into descending.

```python
xs.reverse()
```

```elixir
Enum.reverse(xs)
```

```elixir
reverse xs
```

---

#### Rotate
Return `xs` rotated to left by 2.

```python
n = 2 % len(xs)
res = xs[n:]
res.extend(xs[:n])
res
```
```elixir
n = rem(2, length(xs))
Enum.drop(xs, n) ++ Enum.take(xs, n)
```
```elixir
rotate n xs
```

---

### \[\[ digression ]]

---

![[Pasted image 20240126170438.png]]

`rotate` can be implemented using `reverse`.

---

![[Pasted image 20240126170529.png]]

Your split determining how much you want to rotate

---
<grid flow="col">
![[Pasted image 20240126170944.png|400x50]] 
![[Pasted image 20240126171244.png|350x75]]
![[Pasted image 20240126171715.png]]
J, BQN, and APL
</grid>

note: Array languages notice this parallel which is why Reverse and Rotate usually share the same glyph/function name.

---

### \[\[ end of digression ]]

---

#### Sort
Return the 3 highest values in `xs`.

```python
xs.sort(reverse=True)  # descending sort
xs[3:]
```

```elixir
xs
|> Enum.sort(:desc)
|> Enum.take(3)
```

```elixir
xs
select fall .
take 3
```

---

#### Nub/Deduplicate
Given a list of `keys`, return all unique keys.

```python
list(set(keys))  # doesn't retain order
```

```elixir
Enum.uniq(keys)
```

```elixir
dedup keys
```

---

### Higher-order Functions

note: Now we reach the part of the talk where we start discussing patterns that utilize functions themselves as arguments. Sometimes called as callback or curried functions.

---

#### Map
Return a list containing the numbers 5 to 10 squared.

```python
[x**2 for x in range(5,11)]
```

```elixir
Enum.map(5..10, fn a -> a ** 2)
```

```elixir
range 11
drop 5
pow 2

# * . + 5 range 5
```

---

### \[\[ digression ]]

note: Now you might be thinking, if these patterns are so universal, then how would you even take advantage of these in languages that are much more low-level and lacking in terms of built-in algorithms such as map? Or even the capability of passing functions as arguments in general, like C?

---

```c
#include <stdio.h>
#include <math.h>

int main(void) {
    int i, xs[6];
    for (i = 0; i < 6; i++)   // range
        xs[i] = i+5;
    for (i = 0; i < 6; i++)   // map
        xs[i] = (int) pow(xs[i], 2);

    for (i = 0; i < 6; i++)
        printf("%d ", xs[i]);
    return 0;
}
```

:::  The patterns emerge...

note: Moreover, callback functions DO exist in C, in the form of function pointers. Functions, like the rest of your code, reside in memory locations, which is how C handles higher-order functions, passing the function addresses.

---

```c
#include <stdio.h>
#include <math.h>

int  sqr(int n) { return (int) pow(n, 2); }

void range(int* xs, int s, int e) { 
    while (s <= e) *xs++ = s++;
}

void map(int* xs, int n, int f(int)) {
    for (int i = 0; i < n; i++) xs[i] = f(xs[i]);
}

int main(void) {
    int xs[6];
    range(xs, 5, 10);
    map(xs, 6, &sqr);

    for (int i = 0; i < 6; i++) {
        printf("%d ", xs[i]);
    }
}
```

---
![[Pasted image 20240125175646.png]]
In array languages, invalid shapes throw an exception.

note: Moreover-- Well that's just a massive drawback to array languages then. Except it's not.
This problem has already come up in languages like C too, and their solution?

---
![[Pasted image 20240125175949.png]]

::: Pointers!

note: Use pointers and references. Now we aren't violating any shape rules, as we no longer have an array of conflicting shapes, we now have an array of pointers.  And as you may know from C, this is allowed as this lets us define a definite size for our array, the sum of the size of the pointers.

---

### \[\[ end of digression ]]

---

#### IndexOf

Given two lists, `morse` and `english` where conversions share the same index, convert a message from morse code (a list of tokens) to English.

```python
[ english[ morse.index(letter) ] for letter in message ]
```

```elixir
for letter <- message do
  Enum.at(english, Enum.find_index(morse, letter))
end
```

```elixir
select : english indexof message morse
```

note: halfway there

---
#### Fold/Reduce
Return the factorial of a number `n`.

```python
reduce(op.mul, range(1,n+1))
```

```elixir
Enum.reduce(1..n, &Kernel.*/2)
```

```elixir
/* + 1 range n
```

note: I have some visualizations of this right after I finish all of the remaining functions.

---

### \[\[ digression ]]

---

#### Recursion

```elixir
def factorial1(0), do: 1                    # base case
def factorial1(n), do: n * factorial1(n-1)
```

This code can overflow the stack.

note: Recursion, chances are you've learned about it as a function just calling itself. However, there's actually an extra bit of intricacy that gets lost when we water it down to that definition. And it's with how we do the recursion itself. Here we have the expected implementation for a recursive factorial, we say that this is in head-recursive form.

---

```elixir
def factorial2(n, acc \\ 1)       # function signature
def factorial2(0, acc), do: acc   
def factorial2(n, acc), do: factorial2(n-1, acc * n)
```

This code never overflows the stack.

note: This is the same function, in tail-recursive form. It's still recursion, but written a little bit differently, and if you notice the pattern has a parallel to a reduce.

As you may have learned, recursive calls get put on this thing we call the "call stack," from where the name StackOverflow came from. If you get deep enough with recursion, your computers memory will just give up. But, in functional languages, instead of putting a new stack frame onto the stack when tail-recursion happens, they just reuse the current stack frame resulting in no new allocations.

---
Head-recursion
```elixir
# factorial1(3)
# 3 * factorial1(2)
# 3 * 2 * factorial1(1)
# 3 * 2 * 1 * factorial1(0)
# 3 * 2 * 1 * 1
# 6
```
Tail-recursion
```elixir
# factorial2(3, 1)  -- 1 is a default argument
# factorial2(2, 3)  -- 3 * 1
# factorial2(1, 6)  -- 2 * 3
# factorial2(0, 6)  -- 6 * 1
# 6
```

---

### \[\[ end of digression ]]

---

#### Scan
Check if a string has valid parentheses.

```python
def validParentheses(string):
    def f(acc, x): return acc + (1 if x == '(' else -1)
    def pos(x): return x >= 0

    res = list(accumulate(string, f, initial = 0))
    return all(map(pos, res)) and res[-1] == 0
```

```elixir
defp helper("("), do: 1
defp helper(")"), do: -1
def validParentheses(str) do
  res = str
  |> String.graphemes
  |> Enum.map(&helper/1)
  |> Enum.scan(0, & &1+&2)
  Enum.all?(res, & &1>=0) and List.last(res) == 0
end
```

---

```python
f = (
  =@(    # mask of 1 and 0
  -1*2   # mask of 1 and -1
  scan +
  fork (/*>=0|=0 first reverse)
  *      # and
)
```
<pre><code style="font-family: Uiua386"> f ← ×⊃(/×≥0|=0⊢⇌)\+-1×2=@(
</code></pre>

---

#### Zip
Given a list of x, return the list with every element paired with its index.
```python
zip(xs, range(len(xs)))
# enumerate(xs)
```
```elixir
Enum.zip([xs,0..length(xs)])
# Enum.with_index(xs)
```
```elixir
couple fork id (range length) xs
```

---

#### Brevity

note: If you've been following along on the GitHub handout, I'll be skipping over some functions that aren't that relevant in non-array languages, but I'll cover them later if they come up. Namely: *Transpose*, *Keep*, *Replicate*, *Group* and *Partition*

That being said now we are on our last 3 functions to introduce.

---

#### Filter
Return the number of even elements in `xs`
```python
len(list(filter(lambda x: ~x&1, xs)))
```
```elixir
xs
|> Enum.count(&rem(&1,2) == 0) 
# Enum.count/2 is filter followed by length
```
```elixir
/+ not mod 2 xs  
# no filter primitive, we do a map and reduce add
```

---
#### Window/Roll
Return how many times `xs` increases in value.
```python
from itertools import pairwise
sum(map(lambda a: a[0]<a[1], pairwise(xs)))
```
```elixir
xs
|> Enum.chunk_every(2,1,:discard) 
|> Enum.count(fn [a,b] -> a<b end)
```
```elixir
/ + row / > window 2 xs
```

---
#### Table
Return an `n x n` multiplication table.
```python
[[x*y for y in range(1,n+1)] in range(1,n+1)]
```
```elixir
for x <- 1..n, do: (for y <- 1..n, do: x*y)
```
```elixir
table * . n
```

---

And that just about does it!

note: now we'll go over a few visualizations I have prepared. Of course no one expects you to be able to absorb all of that especially if that was the first time you've encountered these functions, but when you do feel comfortable enough with them, I kid you not you'll start to see that most problems, especially easy ones, are just a composition of these aforementioned functions.

Now we'll move on to the Q&A, and to keep it interesting, while we're doing it I'll be taking suggestions on things to try and solve and maybe show the thought process that I take when I approach these problems, especially the ones with elegant list solutions.

---

#### Q&A and Demo

note: Problems:
1.) Show me a formula to compute how many "friday the 13th" are there between year 2000 - 2023. Show your solution.

Given:
A. Jan 1, 2000 is Saturday
B. CY2000 is a leap year

2.) [#18 Maximum Path Sum I - Project Euler](https://projecteuler.net/problem=18)

---

## Thank you!

https://github.com/44mira/list-mastery

https://tinyurl.com/44miraaaa