import csv


def convert_to_utf8(input, output):
    """Convert input of binary file to ouput file in UTF8."""
    f = open(input, encoding='iso-8859-1')
    data = f.read()
    # print(data)

    with open(output, 'w') as f:
        f.write(data)


def read_csv(input):
    """Read input file and count number of rows."""
    rows = []
    # Open file - avengers.csv

    with open(input) as input_file:
        # Create csv reader object
        reader = csv.reader(input_file)

        # extracting each data row one by one
        for row in reader:
            rows.append(row)
        print(rows[161])


def read_csv_dict(input):
    """Read input file and convert to dictionary with DictReader."""
    with open(input) as csvfile:
        input_file = csv.DictReader(csvfile)
        for row in input_file:
            print(row)
    # print(row(161))


def write_csv(input, output):
    """Read input file and modify data values - export to new file."""
    with open(input) as fin:
        dr = csv.DictReader(fin, delimiter=',')
        dr.fieldnames = [name.lower() for name in dr.fieldnames]
        dr.fieldnames = [name.strip('\n').strip('?') for name in dr.fieldnames]
        dr.fieldnames = [name.replace('/', '_') for name in dr.fieldnames]
        # dr.fieldnames contains values from first row of `f`.
        with open(output, 'w') as fou:
            dw = csv.DictWriter(fou, delimiter=',', fieldnames=dr.fieldnames)
            headers = {}
            for n in dw.fieldnames:
                headers[n] = n
            dw.writerow(headers)
            for row in dr:
                dw.writerow(row)


def main():
    """Main funtion for assignment 6, converting Avengers data."""
    convert_to_utf8('../data/raw/avengers.csv',
                    '../data/interim/avengers_processed.csv')
    read_csv('../data/interim/avengers_processed.csv')
    read_csv_dict('../data/interim/avengers_processed.csv')
    write_csv('../data/interim/avengers_processed.csv',
              '../data/processed/avengers_processed.csv')


if __name__ == "__main__":
    main()
