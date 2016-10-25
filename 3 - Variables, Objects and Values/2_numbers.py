# In Python there ara only integers and floats

num = 23
print("id: {}".format(id(num)))
print("type: {}".format(type(num)))
print("value: {}".format(num))

print("---------------------------")

num = 23 / 4  # Normal division (float result)
print("id: {}".format(id(num)))
print("type: {}".format(type(num)))
print("value: {}".format(num))

print("---------------------------")

num = 23 // 4  # Integer division
print("id: {}".format(id(num)))
print("type: {}".format(type(num)))
print("value: {}".format(num))

print("---------------------------")

num = int(23 / 4)  # Explicit cast to int
print("id: {}".format(id(num)))
print("type: {}".format(type(num)))
print("value: {}".format(num))

print("---------------------------")

num = float(23)  # Explicit cast to float
print("id: {}".format(id(num)))
print("type: {}".format(type(num)))
print("value: {}".format(num))

