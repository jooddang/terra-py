from terra.api.client import Client


def get(address: str) -> dict:
    return Client.get(f"/auth/accounts/{address}")
