import json
import os
from typing import List

from src.application.data_getter import get_columns
from src.application.data_reader import read_csv
from src.application.desmenuzar import desmenuzar
from src.application.publisher import publish_dto_fake


def should_get_list_of_strings_with_6_items(cols: List[str]) -> bool:
    return len(cols) == 6


def should_get_last_row_as_json(channel: str) -> bool:
    file = os.path.join('.', 'outputs', f'{channel}.json')
    expected = {"becario_id": "2", "beca": "op", "nombre": "kiko"}
    dto = {}
    with open(file, 'r', encoding='utf-8') as fil:
        data = fil.read()
        dto = json.loads(data)
    return dto == expected


class TestCsvFeature:
    def test_get_columns(self):
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
        """
                Given that I have a csv file
                with this content:
                    uno,dos,tr3s,4tro,5o,ko
                    1,du,tri,hola,mundo,koko
                    2,dev,el,op,errorr,kiko
                And channel called "becados"
                And 3 filters
        """
        file = './files/data.csv'
        channel = 'becados'
        filter_cols = [
            {
                "col": "uno",
                "name": "becario_id"
            },
            {
                "col": "4tro",
                "name": "beca"
            },
            {
                "col": "ko",
                "name": "nombre"
            },
        ]

        # When try to get the columns
        r = read_csv(file)
        desmenuzar(r, filter_cols, publish_dto_fake, channel)
        assert should_get_last_row_as_json(channel)
