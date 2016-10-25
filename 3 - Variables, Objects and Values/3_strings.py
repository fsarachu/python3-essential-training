s = 'This is a string!'  # Single and double quotes are the same
print(s)

print("----------------------")

s = 'This is a string with a \nescape character!'
print(s)

print("----------------------")

s = r"This is a Raw\n string"  # Raw string are not preprocessed, no escape characters are interpreted
print(s)

print("----------------------")

n = 42
s = "This number is inserted with string formatting: {}".format(n)
print(s)

print("----------------------")

# Backslashes are escaping the newlines in the code
s = '''\
This is a triple
quoted string that can
extend multiple lines\
'''
print(s)

print("----------------------")
