s = 'This is a string!'  # Single and double quotes are the same
print(s)

s = 'This is a string with a \nescape character!'
print(s)

s = r"This is a Raw\n string"  # Raw string are not preprocessed, no escape characters are interpreted
print(s)

n = 42
s = "This number is inserted with string formatting: {}".format(n)
print(s)

# First backslash is escaping the newline in the code
s = '''\
This is a triple
quoted string that can
extend multiple lines
'''
print(s)
