from typing import List

from src.application.data_getter import get_columns
from src.application.data_reader import read_csv


def should_get_list_of_strings_with_6_items(cols: List[str]):
    return len(cols) == 6


class TestCsvFeature:
    def test_get_columns(self):
        # Read CSV
        """
        Given that I have a csv file
        with this on the first line:
            uno,dos,tr3s,4tro,5o,ko
        """
        file = './files/data.csv'

        # When try to get the columns
        r = read_csv(file)
        cols = get_columns(r)

        # Then I get this output:
        # ['uno', 'dos', 'tr3s', '4tro', '5o', 'ko']
        assert should_get_list_of_strings_with_6_items(cols)

    def test_publish_csv(self):
        pass
