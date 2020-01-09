import json
import logging
from json.decoder import JSONDecodeError
from typing import Dict, Optional

import requests

from terra.api import ApiNetwork
from terra.exceptions import ApiError

_log = logging.getLogger(__name__)


class Client:
    def __init__(self, api_network=ApiNetwork.MAINNET):
        self.api_network = api_network.value

    def get_account_by_address(self, account_address: str) -> dict:
        return self.get(f"/auth/accounts/{account_address}")

    def get_balance_by_address(self, account_address: str) -> dict:
        return self.get(f"/bank/balances/{account_address}")

    def get_active_denoms(self) -> dict:
        return self.get("/oracle/denoms/actives")

    def get_latest_block(self) -> dict:
        return self.get("/blocks/latest")

    def get_node_info(self) -> dict:
        return self.get("/node_info")

    def get(
        self,
        path: str,
        params: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = 10,
    ) -> dict:
        try:
            resp = requests.get(
                url=f"{self.api_network}{path}", params=params, timeout=timeout
            )
            if resp.status_code != 200:
                raise ApiError(
                    "The endpoint returned an unsuccessful status code "
                    f"{resp.status_code}: {resp.text}"
                )
            _log.debug(f"Got {resp.status_code} from GET {path}")
            return resp.json()
        except requests.exceptions.Timeout:
            raise ApiError(f"The endpoint timed out after {timeout}s.")
        except requests.exceptions.TooManyRedirects:
            raise ApiError(
                "The endpoint exceeded the configured  number of maximum "
                "redirections."
            )
        except requests.exceptions.RequestException as e:
            raise ApiError(f"The endpoint could not be accessed: {e}")
        except JSONDecodeError:
            raise ApiError(f"The endpoint response is not json decodable.")

    def broadcast_tx(self, signed_tx_dump: str) -> dict:
        """Broadcast the tx json dump."""
        return self.post("/txs", json.loads(signed_tx_dump))

    def post(
        self,
        path: str,
        json: Optional[Dict[str, str]],
        params: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = 60,
    ) -> dict:
        try:
            resp = requests.post(
                url=f"{self.api_network}{path}",
                params=params,
                timeout=timeout,
                json=json,
            )
            if resp.status_code != 200:
                raise ApiError(
                    "The endpoint returned an unsuccessful status code "
                    f"{resp.status_code}: {resp.text}"
                )
            _log.debug(f"Got {resp.status_code} from POST {path}")
            return resp.json()
        except requests.exceptions.Timeout:
            raise ApiError(f"The endpoint timed out after {timeout}s.")
        except requests.exceptions.TooManyRedirects:
            raise ApiError(
                "The endpoint exceeded the configured  number of maximum "
                "redirections."
            )
        except requests.exceptions.RequestException as e:
            raise ApiError(f"The endpoint could not be accessed: {e}")
        except JSONDecodeError:
            raise ApiError(f"The endpoint response is not json decodable.")
