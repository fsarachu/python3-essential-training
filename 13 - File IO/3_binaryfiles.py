def read_buffered(file):
    buffer_size = 524288  # 500kb
    return file.read(buffer_size)


in_file = open('kangaroo.jpg', 'rb')
out_file = open('kangaroo_copy.jpg', 'wb')

buffer = read_buffered(in_file)

while len(buffer):
    out_file.write(buffer)
    buffer = read_buffered(in_file)
