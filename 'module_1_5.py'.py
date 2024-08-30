immutable_var= tuple[1, 2, 'a', 'b']
print(immutable_var)
immutable_var [1]=10
print(immutable_var)
#кортеж не поддерживает обращение по элементам
mutable_list = [3, 4, 'b', 'c']
print(mutable_list)
mutable_list [1] =9
print(mutable_list)