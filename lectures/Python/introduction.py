
# single line comment
"""
Multi
line
comment
"""

'''
Python features:
    - simple syntax
        - minimal bracets
        - indentation
        - clear working with datatypes
        - open sources, many libraries
        - written like the english language ie  and, or, is
'''

my_num = 4
my_str = 'today'

print(my_num)
print(type(my_str))

my_dict = {}
print(type(my_dict))

print(my_str.upper())

my_dict['name'] = "Phil"
print(my_dict)

my_list = []
print(type(my_list))
my_list.append('tomorrow')
my_list.append(7)
my_list.append(False)
my_list.append(5)
print(my_list[0])

print('-'*90)
for val in my_list:
    print(val)
    if val == False:
        print("i'm not true")
print('-'*90)


my_list[0] = 66
my_list.pop()
print(my_list)
my_list.pop(1)
print(my_list)

my_tup = (True, 7)
print(my_tup)
print(my_tup[0])
# my_tup[0] = False

x,y = 2,3
print(x)
print(y)

x = 2,4
print(type(x))

for num in x:
    print(num)

def my_func():
    pass

if 1==2:
    pass