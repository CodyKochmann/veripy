# veripy
Shorthand asserts for those who love predictable code but don't have time for writing every assert in the world.

##### Current Version: 2017.01.19

---

### Installation

```pip install veripy```

### Methods

| Name | Asserts the argument is: | Example Usage |
| :--- | :--- | :--- |
| `veripy.function()` | function | `veripy.function(lambda:"hello")` |
| `veripy.type()` | type | `veripy.type(type(0))` |
| `veripy.str()` | str | `veripy.str("hello world")` |
| `veripy.float()` | float | `veripy.float(0.0)` |
| `veripy.int()` | int | `veripy.int(3)` |
| `veripy.list()` | list | `veripy.list(['hello world'])` |
| `veripy.dict()` | dict | `veripy.dict({"hello":"world"})` |
| `veripy.tuple()` | tuple | `veripy.tuple((1,2,3,4))` |
| `veripy.bytearray()` | bytearray | `veripy.bytearray(bytearray("hello"))` |
| `veripy.iterable()` | iterable | `veripy.not_empty([1,2,3,4])` |
| `veripy.not_empty()` | not empty | `veripy.is_empty([])` |
| `veripy.is_empty()` | empty | `veripy.iterable(range(4))` |
| `veripy.contains_only()` | iterable and contains only one type | `veripy.contains_only([1,2,3,4], int)` |
| `veripy.any_of()` | one of the following types | `veripy.any_of(4, int, float)` |
| `veripy.dir_path()` | path to an existing directory | `veripy.dir_path("./", "../")` |
| `veripy.file_path()` | path to an existing file | `veripy.file_path("veripy.py", "./test.py")` |
| `veripy.file()` | file | `veripy.file(open("test.py","r"), open("veripy.py","r"))` |
| `veripy.generator()` | generator | `veripy.generator((i for i in range(1)))` |
| `veripy.empty_generator()` | generator with no `.next()` value | `veripy.empty_generator((i for i in range(0)))` |

### Upcoming Features Being Considered:

| Name | Description |
| :--- | :--- |
| `veripy.true(args)` | asserts that the argument is `True` |
| `veripy.false(args)` | asserts that the argument is `False` |
| `veripy.none(args)` | asserts that the argument is `None` |
| `veripy.eq(i, args)` | asserts that all arguments equal the value of the first |
