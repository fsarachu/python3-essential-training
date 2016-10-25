choices = dict(
    one='first',
    two='second',
    three='third',
    four='fourth'
)

v = 'six'

print(choices.get(v, 'other'))
