from typing import Dict, Optional
from json.decoder import JSONDecodeError

import requests

from terra.exceptions import ApiError


class Client:
    URL = "https://lcd.terra.dev"
    SESSION = requests.Session()

    @staticmethod
    def get(
        path: str,
        params: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = 5,
    ) -> dict:
        try:
            resp = Client.SESSION.get(
                url=f"{Client.URL}{path}", params=params, timeout=timeout
            )
            if resp.status_code != 200:
                raise ApiError(
                    "The endpoint returned an unsuccessful status code: "
                    f"{resp.text}"
                )
            return resp.json()
        except requests.exceptions.Timeout:
            raise ApiError("The endpoint timed out.")
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
        timeout: Optional[int] = 10,
    ) -> dict:
        try:
            resp = Client.SESSION.post(
                url=f"{Client.URL}{path}",
                params=params,
                timeout=timeout,
                json=json,
            )
            if resp.status_code != 200:
                raise ApiError(
                    "The endpoint returned an unsuccessful status code: "
                    f"{resp.text}"
                )
            return resp.json()
        except requests.exceptions.Timeout:
            raise ApiError("The endpoint timed out.")
        except requests.exceptions.TooManyRedirects:
            raise ApiError(
                "The endpoint exceeded the configured  number of maximum "
                "redirections."
            )
        except requests.exceptions.RequestException as e:
            raise ApiError(f"The endpoint could not be accessed: {e}")
        except JSONDecodeError:
            raise ApiError(f"The endpoint response is not json decodable.")
