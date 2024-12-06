def count_calls(func):
    def wrapper(*args,**kwargs):
        global calls
        calls += 1

        return func(*args, **kwargs)
    return wrapper

@count_calls
def string_info(string:str):
    return len(string), string.upper(), string.lower()

@count_calls
def is_contains(string:str, list_to_search:list):
    lst = list(map(str.upper,list_to_search))
    return string.upper() in lst

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Urban University'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)