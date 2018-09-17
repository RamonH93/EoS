import os

path = 'C:/Users/thbon/PycharmProjects/EoS/data/'

for filename in os.listdir(path):
    if 'parsed' not in filename:
        new_filename = 'parsed_' + filename
        write_file = open(path + new_filename, 'wb')
        with open(path + filename, 'rb') as read_file:
            for line in read_file:
                line = line[1:-2]
                line = line.replace(b'"', b'""')
                line = b'"' + line.replace(b'"",""', b'","') + b'"\n'
                write_file.write(line)
