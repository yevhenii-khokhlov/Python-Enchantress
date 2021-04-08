from dataclasses import dataclass


@dataclass()
class NoSuchId(Exception):
    id: int

    def __str__(self):
        return f'no such id = {self.id}'
