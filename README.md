# prequire
Shorthand asserts for those who love predictable code but dont have time for writing every assert in the world.

### Methods

| Name | Asserts that the argument is: | Example Usage |
| :--- | :--- | :--- |
| `prequire.function()` | function | `prequire.function(lambda:"hello")` |
| `prequire.type()` | type | `prequire.type(type(0))` |
| `prequire.str()` | str | `prequire.str("hello world")` |
| `prequire.float()` | float | `prequire.float(0.0)` |
| `prequire.int()` | int | `prequire.int(3)` |
| `prequire.list()` | list | `prequire.list(['hello world'])` |
| `prequire.dict()` | dict | `prequire.dict({"hello":"world"})` |
| `prequire.tuple()` | tuple | `prequire.tuple((1,2,3,4))` |
| `prequire.bytearray()` | bytearray | `prequire.bytearray(bytearray("hello"))` |
| `prequire.iterable()` | iterable | `prequire.not_empty([1,2,3,4])` |
| `prequire.not_empty()` | not empty | `prequire.is_empty([])` |
| `prequire.is_empty()` | empty | `prequire.iterable(range(4))` |
| `prequire.contains_only()` | iterable and contains only one type | `prequire.contains_only([1,2,3,4], int)` |
| `prequire.any_of()` | one of the following types | `prequire.any_of(4, int, float)` |

### Upcoming Features:

| Name | Description |
| :--- | :--- |
| `prequire.dir_path()` | confirms that the given string is a path to a directory |
| `prequire.file_path()` | confirms that the given string is a path to a file |
| `prequire.file()` | confirms that the given object is a file |
