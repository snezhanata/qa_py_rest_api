import requests
from pprint import pprint
from pytest_voluptuous import S
from requests import Response

from schemas.schemas import get_single_user_schema
from utils.base_session import reqres_session


def test_get_single_user_schema():
    result: Response = reqres_session().get(url="/api/users/2")

    assert result.status_code == 200
    assert result.json()["data"]["id"] == 2
    assert result.json()["data"]["first_name"] == "Janet"
    assert result.json()["data"]["last_name"] == "Weaver"
    assert result.json()["data"]["avatar"] == "https://reqres.in/img/faces/2-image.jpg"
    assert result.json()["data"]["email"] == "janet.weaver@reqres.in"
    assert result.json()["support"]["url"] == "https://reqres.in/#support-heading"
    assert (
        result.json()["support"]["text"]
        == "To keep ReqRes free, contributions towards server costs are appreciated!"
    )
    assert result.json() == S(get_single_user_schema)
    print("\n")
    pprint(result.json())
