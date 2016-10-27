# In Python there ara only integers and floats

num = 23
print("value: {}".format(num))
print("type: {}".format(type(num)))

print("---------------------------")

num = 23 / 4  # Normal division (float result)
print("value: {}".format(num))
print("type: {}".format(type(num)))

print("---------------------------")

num = 23 // 4  # Integer division
print("value: {}".format(num))
print("type: {}".format(type(num)))

print("---------------------------")

num = int(23 / 4)  # Explicit cast to int
print("value: {}".format(num))
print("type: {}".format(type(num)))

print("---------------------------")

num = float(23)  # Explicit cast to float
print("value: {}".format(num))
print("type: {}".format(type(num)))

