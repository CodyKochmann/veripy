# veripy
Shorthand asserts for those who love predictable code but dont have time for writing every assert in the world.

### Methods

| Name | Asserts that the argument is: | Example Usage |
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

### Upcoming Features:

| Name | Description |
| :--- | :--- |
| `veripy.dir_path()` | confirms that the given string is a path to a directory |
| `veripy.file_path()` | confirms that the given string is a path to a file |
| `veripy.file()` | confirms that the given object is a file |
