# require.py
Shorthand asserts for those who love predictable code but dont have time for writing every assert in the world.

### Methods

| Name | Asserts that the argument is: | Example Usage |
| :--- | :--- | :--- |
| require.function() | function | require.function(lambda:"hello") |
| require.type() | type | require.type(type(0)) |
| require.str() | str | require.str("hello world") |
| require.float() | float | require.float(0.0) |
| require.int() | int | require.int(3) |
| require.list() | list | require.list(['hello world']) |
| require.dict() | dict | require.dict({"hello":"world"}) |
| require.tuple() | tuple | require.tuple((1,2,3,4)) |
| require.bytearray() | bytearray | require.bytearray(bytearray("hello world")) |
| require.iterable() | iterable | require.not_empty([1,2,3,4]) |
| require.not_empty() | not empty | require.is_empty([]) |
| require.is_empty() | empty | require.iterable(range(4)) |
| require.contains_only() | iterable and contains only one type | require.contains_only([1,2,3,4], int) |
| require.any_of() | one of the following types | require.any_of(4, int, float) |
