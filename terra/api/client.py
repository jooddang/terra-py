from typing import Dict, Optional
from json.decoder import JSONDecodeError
import logging

import requests

from terra.exceptions import ApiError

_log = logging.getLogger(__name__)


class Client:

    def __init__(self, testnet=False):
        if testnet:
            self.URL = "https://vodka-lcd.terra.dev"
        else:
            self.URL = "https://lcd.terra.dev"

    @staticmethod
    def get(
        path: str,
        params: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = 10,
    ) -> dict:
        try:
            resp = requests.get(
                url=f"{Client.URL}{path}", params=params, timeout=timeout
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

    @staticmethod
    def post(
        path: str,
        json: Optional[Dict[str, str]],
        params: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = 60,
    ) -> dict:
        try:
            resp = requests.post(
                url=f"{Client.URL}{path}",
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
