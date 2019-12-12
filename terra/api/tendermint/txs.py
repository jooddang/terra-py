import json

from terra.api.client import Client


def post(tx_dump: str) -> dict:
    """Broadcast the tx json dump."""
    return Client.post("/txs", json.loads(tx_dump))
