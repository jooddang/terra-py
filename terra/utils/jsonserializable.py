import json


class JsonSerializable:

    def to_json(self) -> str:
        return json.dumps(self.__dict__, default=lambda o: o.__dict__)
