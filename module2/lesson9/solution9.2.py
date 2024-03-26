d = input('RGB: ').split(', ')
def convert_to_hex(r, g, b):
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)
hex = convert_to_hex(int(d[0]), int(d[1]), int(d[2]))
print(hex)

# 255, 0, 0
# 0, 255, 0
# 0, 0, 255
