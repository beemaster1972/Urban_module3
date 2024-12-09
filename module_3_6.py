def calculate_result(value):
    if type(value) == str:
        return len(value)
    elif isinstance(value, (int, float)):
        return value


def calculate_structure_sum(*args,res=0, **kwargs):

    for arg in args:
        if isinstance(arg, (str, int)):
            res += calculate_result(arg)
        if isinstance(arg, (list, tuple,set)):
            res += calculate_structure_sum(*arg)
        if isinstance(arg,dict):
            res += calculate_structure_sum(**arg)
    for key,val in kwargs.items():
        res += (calculate_result(key) + calculate_result(val))
    return res

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
