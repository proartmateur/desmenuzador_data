import json
import os


def publish_dto(dto: dict, channel: str):
    # implementar Rabbit MQ
    print(f"Publising to: {channel}")
    print(dto)
    print(" ")


def publish_dto_fake(dto: dict, channel: str):
    print(f"Publising to: {channel}")
    print(dto)
    print(" ")
    file = os.path.join('.', 'outputs', f'{channel}.json')
    with open(file, 'w', encoding='utf-8') as fil:
        fil.write(json.dumps(dto))
