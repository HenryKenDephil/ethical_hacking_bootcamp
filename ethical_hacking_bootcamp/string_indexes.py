selfish = '01234567'

#indexing techniques or string slicing are as shown below
#[start:end]
#[start:stop:stepover]

print('this is first index', selfish[0])

print('start from index 1 and stop at index 3', selfish[1:3])
print('start at index zero and stop at index 8 with stepover of 2', selfish[0:8:2])
print('start an index 1 and stop at last index', selfish[1:])
print('reverse the order', selfish[::-1])