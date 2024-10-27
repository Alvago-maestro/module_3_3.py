def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [False, 'stone', 5]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
values_list_2 = [1, 'summer']
print_params()
print_params(8, 15)
print_params(False, 2, 'cat')
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)