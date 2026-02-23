# typing — Support for type hints

The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc.

### Type aliases
A type alias is defined using the type statement, which creates an instance of TypeAliasType.

```
type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```

Or marked with TypeAlias to make it explicit that this is a type alias, not a normal variable assignment:
```
from typing import TypeAlias
Vector: TypeAlias = list[float]
```

### NewType
Use the NewType helper to create distinct types:
```
from typing import NewType
UserId = NewType('UserId', int)
some_id = UserId(524313)
```
The static type checker will treat the new type as if it were a subclass of the original type.

### Annotating callable objects
To annotate callable objects in Python, use the Callable type from the collections.abc module, or typing.Callable in older code. The annotation specifies both the argument types and the return type of the callable object. 

```
from collections.abc import Callable
def apply_func(a: int, b: int, func: Callable[[int, int], int]) -> int:
    return func(a, b)
def add(x: int, y: int) -> int:
    return x + y
result = apply_func(4, 5, add)
```

### Generics
A form of type hinting that allows functions, classes, and methods to operate on multiple data types while preserving type information and ensuring type consistency

```
from collections.abc import Sequence
def first[T](l: Sequence[T]) -> T:  # Function is generic over the TypeVar "T"
    return l[0]
```

### Annoting tuple
Tuples in Python can be annotated to specify the types and number of their elements
```
from typing import Tuple
my_tuple: Tuple[int, str, bool] = (1, "hello", True)
```

### the type of class objects
In Python, classes are themselves objects, and the type of these class objects is type. 
This means that type is a metaclass—a class whose instances are classes. When you define a class in Python using the class keyword, the Python interpreter dynamically creates an instance of the type metaclass. 

### Annotating generators and coroutines
Coroutines are specialized functions that allow execution to be paused and resumed at specific points, which enables cooperative multitasking within a single thread.

A generator can be annotated using the generic type Generator[YieldType, SendType, ReturnType]. 

Example:
```
# have to import Generator class
def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'
```

Async generators are handled in a similar fashion, but don’t expect a ReturnType type argument (AsyncGenerator[YieldType, SendType]).

```
async def infinite_stream(start: int) -> AsyncGenerator[int]:
    while True:
        yield start
        start = await increment(start)
```

Coroutines can be annotated using Coroutine[YieldType, SendType, ReturnType].
```
from collections.abc import Coroutine
c: Coroutine[list[str], str, int]  # Some coroutine defined elsewhere
x = c.send('hi')                   # Inferred type of 'x' is list[str]
async def bar() -> None:
    y = await c                    # Inferred type of 'y' is int
```

### Any type
A special kind of type is Any. A static type checker will treat every type as being compatible with Any and Any as being compatible with every type. No type checking is performed.

```
from typing import Any
def legacy_parser(text: Any) -> Any:
    ...
    return data
```

### Nominal vs structural subtyping
Initially PEP 484 defined the Python static type system as using nominal subtyping. This means that a class A is allowed where a class B is expected if and only if A is a subclass of B that is explicit inheritance.

While structural subtyping (implemented via Protocols) determines compatibility based on the actual methods and attributes an object possesses. 

## typing Module contents

Special typing primitives
- typing.Any
- typing.AnyStr:  meant to be used for functions that may accept str or bytes arguments but cannot allow the two to mix.
- typing.LiteralString: only literal strings.
- typing.Never, typing.NoReturn: Never and NoReturn represent the bottom type, a type that has no members.
- typing.Self: Special type to represent the current enclosed class.
- typing.TypeAlias: Special annotation for explicitly declaring a type alias.

Special forms
- typing.Union: Union type; Union[X, Y] is equivalent to X | Y and means either X or Y.
    
    Ex:
    ```
    type A = Union[int, str]
    Union[A, float] != Union[int, str, float]
    ```
- typing.Optional: Optional[X] is equivalent to X | None (or Union[X, None]).
- typing.Concatenate: Special form for annotating higher-order functions.
- typing.Literal: Literal can be used to indicate to type checkers that the annotated object has a value equivalent to one of the provided literals.
    
    Ex:
    ```
    type Mode = Literal['r', 'rb', 'w', 'wb']
    def open_helper(file: str, mode: Mode) -> str:
        ...
    open_helper('/some/path', 'r')      # Passes type check
    open_helper('/other/path', 'typo')  # Error in type checker
    ```
- typing.ClassVar: Special type construct to mark class variables.
    
    Ex: 
    ```
    class Starship:
        stats: ClassVar[dict[str, int]] = {} # class variable
        damage: int = 10                     # instance variable
    ```
- typing.Final: Special typing construct to indicate final names to type checkers.
- typing.Required: Special typing construct to mark a TypedDict key as required.
- typing.NotRequired: Special typing construct to mark a TypedDict key as potentially missing.
- typing.ReadOnly: A special typing construct to mark an item of a TypedDict as read-only.
- typing.Annotated: Special typing form to add context-specific metadata to an annotation. Ex: T1 = Annotated[int, ValueRange(-10, 5)]
- typing.TypeIs: Special typing construct for marking user-defined type predicate functions.
- typing.TypeGuard: returns value as a boolean. If the return value is True, the type of its argument is the type inside TypeGuard.
- typing.Unpack: Typing operator to conceptually mark an object as having been unpacked.

#### Protocol
defines an implicit interface that specifies the methods and attributes a class must implement to be considered of a certain type, enabling structural subtyping or "static duck typing".

```
# Defining a Protocol
from typing import Protocol
class Logger(Protocol):
    def log(self, message: str) -> None:
        ... # Ellipsis indicates no default implementation
```

#### ABCs and Protocols for working with I/O
class typing.IO[AnyStr]
class typing.TextIO
class typing.BinaryIO

### Functions and decorators
- typing.cast(typ, val): Cast a value to a type.
- typing.assert_type(val, typ, /): Ask a static type checker to confirm that val has an inferred type of typ.
- typing.assert_never(arg, /): Ask a static type checker to confirm that a line of code is unreachable.
- typing.reveal_type(obj, /): Ask a static type checker to reveal the inferred type of an expression.
- @typing.dataclass_transform(*, eq_default=True, order_default=False, kw_only_default=False, frozen_default=False, field_specifiers=(), **kwargs): Decorator to mark an object as providing dataclass-like behavior.
- @typing.overload: Decorator for creating overloaded functions and methods. The @overload decorator allows describing functions and methods that support multiple different combinations of argument types.
- typing.get_overloads(func): Return a sequence of @overload-decorated definitions for func.
- typing.clear_overloads(): Clear all registered overloads in the internal registry.
- @typing.final: Decorator to indicate final methods and final classes.
- @typing.no_type_check: Decorator to indicate that annotations are not type hints.
- @typing.no_type_check_decorator: Decorator to give another decorator the no_type_check() effect.
- @typing.override: Decorator to indicate that a method in a subclass is intended to override a method or attribute in a superclass.
- @typing.type_check_only: Decorator to mark a class or function as unavailable at runtime.

### Introspection helpers
- typing.get_type_hints(obj, globalns=None, localns=None, include_extras=False): Return a dictionary containing type hints for a function, method, module or class object.
- typing.get_origin(tp): Get the unsubscripted version of a type: for a typing object of the form X[Y, Z, ...] return X
- typing.get_args(tp): Get type arguments with all substitutions performed: for a typing object of the form X[Y, Z, ...] return (Y, Z, ...).
    
    Examples:
    ```
    assert get_args(int) == ()
    assert get_args(Dict[int, str]) == (int, str)
    ```
- typing.get_protocol_members(tp): Return the set of members defined in a Protocol.
- typing.is_protocol(tp): Determine if a type is a Protocol.
- typing.is_typeddict(tp): Check if a type is a TypedDict.

### Constant
- typing.TYPE_CHECKING: A special constant that is assumed to be True by 3rd party static type checkers. It’s False at runtime.
 




























