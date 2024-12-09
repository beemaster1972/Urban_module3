def print_params(a=1, b='string', c=True):
    print(f'a={a}, b={b}, c={c}')
    print('Default: ', *print_params.__defaults__)


values_list = [100.0, 10, 'abrakadabra']
values_dict = {'a': 2, 'b': False, 'c': 2.5}
print_params()
print_params(3)
print_params('!!!', True)
print_params(5, 4, 1)
print_params(b=25)
print_params(c=[1,2,3])
print_params(*values_list)
print_params(**values_dict)
values_list = [4,(1,2)]
print_params(*values_list,42)
