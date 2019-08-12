import json


class JsonSerializable(object):

    def to_json(self):
        json.dumps(self.__dict__, default=lambda o: o.to_json())
