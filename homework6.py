my_dict = {'Dima': 1980, 'Alex': 1993, 'Ivan': 2004, 'John': 1964}
print('\nСловарь my_dict:\n', my_dict, '\n')
print('Год рождения Alex:', my_dict['Alex'])
my_dict.update({'Voland': 1657, 'Gebi': 1967})
print('Год рождения Dima(покидает на словарь=():', my_dict.pop('Dima'), '\n')
print('Обновленный словарь my_dict:\n', my_dict, '\n')

my_set = {1, 42, 2, 'qwerty', 4.5, True,1 , 3, 5, 42, True,1 , 3, 5 , 1, 1, 1}
print('Элементы множества my_set:\n', my_set)
my_set.add(123)
my_set.add('qwer')
my_set.discard(1)
print('Обновленное множество my_set:\n', my_set)
