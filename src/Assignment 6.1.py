import sys
import csv
import distutils


def convert_to_utf8(input, output):
    f = open(input, encoding='iso-8859-1')
    data = f.read()
    #print(data)

    with open(output, 'w') as f:
        f.write(data)


def read_csv(input):
    rows = []
    # Open file - avengers.csv

    with open('../data/interim/avengers_utf8.csv') as input:
    # Create csv reader object
        reader = csv.reader(input)

    # extracting each data row one by one
        for row in reader:
            rows.append(row)
        print(rows[161])


def read_csv_dict(input):
    with open(input) as csvfile:
        input_file = csv.DictReader(csvfile)
        for row in input_file:
            print(row)
    #print(row(161))


def write_csv(input,output):
    with open(input) as fin:
        dr = csv.DictReader(fin, delimiter=',')
        dr.fieldnames = [name.lower() for name in dr.fieldnames]
        dr.fieldnames = [name.strip('\n').strip('?') for name in dr.fieldnames]
        dr.fieldnames = [name.replace('/','_') for name in dr.fieldnames]
# dr.fieldnames contains values from first row of `f`.
        with open(output,'w') as fou:
            dw = csv.DictWriter(fou, delimiter=',', fieldnames=dr.fieldnames)
            headers = {}
            for n in dw.fieldnames:
                headers[n] = n
            dw.writerow(headers)
            for row in dr:
                dw.writerow(row)


def main():
    convert_to_utf8('../data/raw/avengers.csv','../data/interim/avengers_utf8.csv')
    read_csv('../data/interim/avengers_utf8.csv')
    read_csv_dict('../data/interim/avengers_utf8.csv')
    write_csv('../data/interim/avengers_utf8.csv','../data/processed/avengers_utf8.csv')


if __name__ == "__main__":
    main()
