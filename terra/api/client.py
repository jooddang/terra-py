from typing import Dict, Optional
import json

import requests

from terra.api.exceptions import ApiError


class Client:
    URL = "https://lcd.terra.dev"

    @staticmethod
    def get(path: str, params: Optional[Dict[str, str]] = None) -> dict:
        try:
            resp = requests.get(url=f"{Client.URL}{path}", params=params)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError:
            raise ApiError(
                "The endpoint returned an unsuccessful status code."
            )
        except requests.exceptions.Timeout:
            raise ApiError("The endpoint timed out.")
        except requests.exceptions.TooManyRedirects:
            raise ApiError(
                "The endpoint exceeded the configured  number of maximum "
                "redirections."
            )
        except requests.exceptions.RequestException as e:
            raise ApiError(f"The endpoint could not be accessed: {e}")
        except json.decoder.JSONDecodeError:
            raise ApiError(f"The endpoint response is not json decodable.")

    @staticmethod
    def post(
        path: str,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, str]] = None,
    ) -> dict:
        try:
            resp = requests.get(url=f"{Client.URL}{path}", params=params)
            resp.raise_for_status()
            return resp
        except requests.exceptions.HTTPError:
            raise ApiError(
                "The endpoint returned an unsuccessful status code."
            )
        except requests.exceptions.Timeout:
            raise ApiError("The endpoint timed out.")
        except requests.exceptions.TooManyRedirects:
            raise ApiError(
                "The endpoint exceeded the configured  number of maximum "
                "redirections."
            )
        except requests.exceptions.RequestException as e:
            raise ApiError(f"The endpoint could not be accessed: {e}")
        except json.decoder.JSONDecodeError:
            raise ApiError(f"The endpoint response is not json decodable.")
