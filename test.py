# basic print() function
values=["one", "two", "three", "four", "five"]
print(*values)

# use the 'sep' argument to control the separator between values:
print(*values, sep=' -- ')

# use the 'end' argument to control the line ending characters
# let's auto-print the current line number along with each item!
for i in range(0, len(values)):
    print(values[i], end=f" [line: {str(i+1)}]\n")