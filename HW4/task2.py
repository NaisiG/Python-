'''def key_params(**kwargs) -> dict:
    result = dict()
    for k, v in kwargs.items():
        try:
            _ = hash(v)
            result[v] = k
        except TypeError:
            result[str(v)] = k

    return result
'''
# Решение с сайта:

def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, str, float, bool, tuple)):
            result[value] = key
        else:
            result[str(value)] = key
    return result
params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}
# {None: 'a', '': 'b', '[]': 'c', '{}': 'd'}
# Вводимые значения: a = None, b = '', c = [], d = {}
# Вводимые значения:a=1, b='hello', c=[1, 2, 3], d={}
