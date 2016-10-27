choices = dict(
    one='first',
    two='second',
    three='third',
    four='fourth'
)

v = 'six'

print(choices.get(v, 'other'))  # Return the value for the key inside 'v', if it doesnt exist return 'other'
