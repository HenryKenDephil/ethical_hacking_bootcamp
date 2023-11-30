#formatted strings use f at the begining in python3
name = 'Johnny'
age = 55


print(f'hello {name}. You are {age} years old')

#in python2, string formatting was done using .format() function

print('hi {}. You are {} years old'.format(name, age))
print('hi {new_name}. You are {new_age} years old'.format(new_name='Kevin', new_age=28))

#nb, always use the f string format\
#  for python3 in the first example

