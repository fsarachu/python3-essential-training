buffer_size = 524288  # 500kb

in_file = open('kangaroo.jpg', 'rb')
out_file = open('kangaroo_copy.jpg', 'wb')

buffer = in_file.read(buffer_size)

while len(buffer):
    out_file.write(buffer)
    buffer = in_file.read(buffer_size)
