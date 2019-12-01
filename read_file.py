


'''
# open file for read.
open("README.md", "r")

# write the file.
open("README.md", "w")

# append information at the end of file.
open("README.md", "a")

# read and write the file.
open("README.md", "r+")
'''

file = open("README.md", "r")
print(file.readable())

# read all lines and put them into an array;
#print(file.readlines()[2])

for line in file.readlines():
    print(line)

# always close the file.
file.close()



