# Mary Kay Kincaid
# 4/25/18
# Midterm Assignment

# imports


# functions used in this .py file
from msds510.util import read_csv_dict
from msds510.util import create_report


# main function
def main():
    read_csv_dict('../data/processed/avengers_processed.csv')
    create_report('../data/processed/avengers_sorted.csv')


if __name__ == "__main__":
    main()
