# Python Dataclasses

Data classes are just regular classes that are geared towards storing state, rather than containing a lot of logic. Every time you create a class that mostly consists of attributes, you make a data class.

What the dataclasses module does is to make it easier to create data classes. It takes care of a lot of boilerplate for you.

### What are python dataclasses?
Dataclasses are special classes for storing data which uses @dataclass decorator to generate .__init__(), .__repr__(), and .__eq__() automatically. 

Dataclasses allow you to create classes quickly, but you can also add defaults, custom methods, ordering, immutability, inheritance, and even slots.

#### Key features generated automatically by the @dataclass decorator include:
- ```__init__()```: A constructor method for initializing class instances with type hints.
- ```__repr__()```: A developer-friendly string representation of the object for easy debugging.
- ```__eq__()```: An equality method that compares objects based on their data rather than memory location. 

Example:
```
from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str
```

#### namedtuple: 
A namedtuple in Python is a factory function that creates subclasses of the built-in tuple type with named fields, providing a more readable and self-documenting way to work with immutable data.


### Type Hints in Dataclass
adding some kind of type hint is mandatory when defining the fields in your data class. Without a type hint, the field will not be a part of the data class. However, if you do not want to add explicit types to your data class, use typing.Any

Ex:
```
from dataclasses import dataclass
from typing import Any

@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42
```

### More Flexible Data Classes
Ex:
```
from dataclasses import dataclass
from typing import List

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]
```

### Advanced Default value
Ex:
```
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]
```

Data classes use something called a default_factory to handle mutable default values. To use default_factory, you need to use the field() specifier:

```
from dataclasses import dataclass, field
from typing import List

@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)
```

The metadata parameter is not used by the data classes themselves but is available for you (or third party packages) to attach information to fields.
```
from dataclasses import dataclass, field
@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})
```

### Sorted dataclasses
By setting order=True in the @dataclass decorator, Python automatically generates the comparison methods (__lt__, __le__, __gt__, __ge__). The instances are compared as if they were tuples of their fields, in the order the fields are declared in the class. 

```
@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False) # must be the first field
    rank: str
    suit: str
```

### Immutable Data Classes
To make a data class immutable, set frozen=True when you create it.

```
from dataclasses import dataclass
@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0
```

### Inheritance
You can subclass data classes quite freely.
```
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

@dataclass
class Capital(Position):
    country: str
```

Things get a little more complicated if any fields in the base class have default values
The problem is that our new country field has no default value, while the lon and lat fields have default values. The data class will try to write an .__init__() method with the following signature:
```
def __init__(name: str, lon: float = 0.0, lat: float = 0.0, country: str):
```

Another thing to be aware of is how fields are ordered in a subclass. Starting with the base class, fields are ordered in the order in which they are first defined.

## Optimizing Data Classes
Slots can be used to make classes faster and use less memory. Data classes have no explicit syntax for working with slots, but the normal way of creating slots works for data classes as well.

In Python, __slots__ is a special class attribute used to explicitly declare the data members that instances of a class are expected to have

```
from dataclasses import dataclass

@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float

@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float
```


