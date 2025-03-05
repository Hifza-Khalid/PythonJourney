# Python Built-in Data Types Demonstration

# Text Type
text = "Hello, Python!"  # str
print(type(text))  # Output: <class 'str'>

# Numeric Types
integer_num = 10  # int
float_num = 10.5  # float
complex_num = 3 + 4j  # complex

print(type(integer_num))  # Output: <class 'int'>
print(type(float_num))    # Output: <class 'float'>
print(type(complex_num))  # Output: <class 'complex'>

# Sequence Types
my_list = [1, 2, 3]  # list
my_tuple = (1, 2, 3)  # tuple
my_range = range(5)  # range

print(type(my_list))   # Output: <class 'list'>
print(type(my_tuple))  # Output: <class 'tuple'>
print(type(my_range))  # Output: <class 'range'>

# Mapping Type
my_dict = {"name": "John", "age": 30}  # dict
print(type(my_dict))  # Output: <class 'dict'>

# Set Types
my_set = {1, 2, 3}  # set
my_frozenset = frozenset({1, 2, 3})  # frozenset

print(type(my_set))      # Output: <class 'set'>
print(type(my_frozenset))  # Output: <class 'frozenset'>

# Boolean Type
is_python_fun = True  # bool
print(type(is_python_fun))  # Output: <class 'bool'>

# Binary Types
binary_data = b"Python"  # bytes
byte_array_data = bytearray(5)  # bytearray
memory_view_data = memoryview(bytes(5))  # memoryview

print(type(binary_data))      # Output: <class 'bytes'>
print(type(byte_array_data))  # Output: <class 'bytearray'>
print(type(memory_view_data)) # Output: <class 'memoryview'>

# None Type
nothing = None  # NoneType
print(type(nothing))  # Output: <class 'NoneType'>
