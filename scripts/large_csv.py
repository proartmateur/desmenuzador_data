import csv

from src.application.data_getter import get_columns, get_rows
from src.application.data_reader import read_csv

if __name__ == "__main__":
    file = './data.csv'
    file_l = './data_large.csv'
    r = read_csv(file)
    cols = get_columns(r)
    rows = get_rows(r)

    with open(file_l, mode='w') as large_file:
        large_writer = csv.writer(large_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        large_writer.writerow(cols)
        for row in rows:
            for i in range(0, 100):
                large_writer.writerow(row)
