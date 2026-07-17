# Python

## Converting an Integer into Decimals
```python
from decimal import Decimal
a = 10
print(type(Decimal(a)))
```

## Converting an String of Integers into Decimals
```python
# Converting an String of Integers into Decimals
from decimal import Decimal
a = "12345"
a = Decimal(a)
print(a)
print(type(a))
```

## Reversing a String using an Extended Slicing Technique
```python
a = "A goat gets killed"
rev = a[::-1]
print(rev)
```

## Counting Vowels in a Given Word
```python
word = "paracetamol"
cnt = 0
for i in word:
    if i in ['a', 'e', 'i', 'o', 'u']:
        cnt = cnt + 1
print(cnt)
```

## Counting the Number of Occurances of a Character in a String
```python
str = "A brown fox becomes darker due to heAvy sunshine and uv radiation"
char_to_find = 'a'
cnt = 0
for i in str:
    if i.lower() == char_to_find.lower():
        cnt = cnt + 1
print(cnt)
```

## Writing Fibonacci Series
```python
fib = [0,1]
for i in range(5):
    fib.append(fib[-1] + fib[-2])
print(fib)
```

## Finding the Maximum Number in a List
```python
def find_max_no(li : list):
    max = li[0]
    for n in li[1:]:
        if n > max:
            max = n
    return max

print(find_max_no([14, 20, 13, 12, 15]))
```

## Two Sum
Standard(first pair)
```python
arr = [9, 1, 5, 4, 7]
target = 10
# ans = (0,1)
def two_sum(arr, target):
    seen = {}
    result = []
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            return [seen[complement], i]
        seen[arr[i]] = i
    return[]
print(two_sum(arr, target))
```

All pairs
```python
arr = [9, 1, 5, 4, 7, 5, 3]
target = 10
def two_sum(arr, target):
    seen = {}
    result = []
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen:
            result.append((seen[complement], i))
        seen[arr[i]] = i
    return result
print(two_sum(arr, target))
```


## 
```python

```

## 
```python

```

## 
```python

```

## 
```python

```

## 
```python

```

## 
```python

```

## 
```python

```

## 
```python

```

