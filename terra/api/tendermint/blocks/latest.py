from terra.api.client import Client


def get() -> dict:
    return Client.get("/blocks/latest")
