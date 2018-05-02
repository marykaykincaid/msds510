def month_string_to_number(string):
    """Convert month names to numbers."""
    m = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except Exception:
        raise ValueError('Not a month')


# main
def main():
    """Main function to convert records into new date format."""
    records = [
        dict(year='1998', intro='Jun-88'),
        dict(year='1989', intro='May-89'),
        dict(year='2005', intro='5-May'),
        dict(year='2013', intro='13-Nov'),
        dict(year='2014', intro='14-Jan'),
    ]
    # today = datetime.date.today()
    month_string_to_number('October')
    print(records)


if __name__ == "__main__":
    main()
