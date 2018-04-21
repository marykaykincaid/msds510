import sys
def convert_to_utf8(input, output):
    f = open(input, encoding='iso-8859-1')
    data = f.read()
    print(data)

    with open(output, 'w') as f:
        f.write(data)

def main():
    convert_to_utf8('../data/raw/avengers.csv','../data/interim/avengers_utf8.csv')

main()
