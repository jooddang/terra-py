from terra.api.client import Client


def get() -> dict:
    return Client.get("/oracle/denoms/actives")
