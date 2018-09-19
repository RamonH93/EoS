import os
import pandas as pd


def parser():
    path = 'D:/Ramon/Documents/Economics of Cyber Security 2019/phishing/'

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
            write_file.close()

    write_file = open(path + 'parsed_all_phishing.csv', 'wb')
    first_file = True
    for filename in os.listdir(path):
        first_line = True
        if 'parsed' in filename and 'from' in filename:
            with open(path + filename, 'rb') as read_file:
                for line in read_file:
                    if first_line:
                        if not first_file:
                            first_file = False
                            first_line = False
                            continue
                        first_line = False
                    write_file.write(line)
    write_file.close()


def import_csv(path):
    # set pandas output width
    desired_width = 320
    pd.set_option('display.width', desired_width)

    # read dataset
    df = pd.read_csv(path, parse_dates=[2,3], infer_datetime_format=True)

    return df
