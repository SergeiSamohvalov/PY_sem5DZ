# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.


from itertools import groupby

with open('incoming.txt', 'r') as text:
    in_data = text.read()

print(in_data)


def encode(data):
    return [(key, len(tuple(group))) for key, group in groupby(data)]


encode_data = encode(in_data)
print(encode_data)

with open('outcoming.txt', 'w') as text:
    out_data = text.write(str(encode_data))


def decode(data):
    return ''.join(x[0]*x[1] for x in data)


decode_data = decode(encode_data)
print(decode_data)