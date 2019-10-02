from httmock import all_requests, HTTMock
import pytest

from terra import api
from terra import exceptions


@all_requests
def response_200(url, request):
    return {"status_code": 200, "content": '{"test": "test"}'}


@all_requests
def response_404(url, request):
    return {"status_code": 404, "content": ""}


@all_requests
def response_timeout(url, request):
    pass


@all_requests
def response_not_json(url, request):
    return {"status_code": 200, "content": "test"}


def test_client_get_200():
    with HTTMock(response_200):
        assert api.client.Client.get("/") == {"test": "test"}


def test_client_get_404():
    with HTTMock(response_404):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.get("/")
            assert e.match("404")


def test_client_get_timeout():
    with HTTMock(response_timeout):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.get("/")
            assert e.match("timed out")


def test_client_get_not_json():
    with HTTMock(response_not_json):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.get("/")
            assert e.match("json")


def test_client_post_200():
    with HTTMock(response_200):
        assert api.client.Client.post("/") == {"test": "test"}


def test_client_post_404():
    with HTTMock(response_404):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.post("/")
            assert e.match("404")


def test_client_post_timeout():
    with HTTMock(response_timeout):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.post("/")
            assert e.match("timed out")


def test_client_post_not_json():
    with HTTMock(response_not_json):
        with pytest.raises(exceptions.ApiError) as e:
            api.client.Client.post("/")
            assert e.match("json")


def test_get_tendermint_node_info():
    assert list(api.tendermint.node_info.get().keys())[0] == "protocol_version"


def test_get_oracle_denoms_actives():
    assert list(api.oracle.denoms.actives.get().keys())[0] == "actives"
