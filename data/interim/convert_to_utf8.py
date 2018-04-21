import sys
def main(input, output):
    f = open(input, encoding='iso-8859-1')
    data = f.read()
    #print(data)

    with open(output, 'w') as f:
        f.write(data)

main('../raw/avengers.csv','../processed/avengers_utf8.csv')
