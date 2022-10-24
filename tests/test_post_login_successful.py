import requests
from pprint import pprint
from pytest_voluptuous import S
from requests import Response

from schemas.schemas import post_login_successful
from utils.base_session import reqres_session


def test_get_single_user_schema():
    email = "eve.holt@reqres.in"
    password = "cityslicka"

    result: Response = reqres_session().post(
        url="/api/login", json={"email": email, "password": password}
    )

    assert result.status_code == 200
    assert result.json()["token"] == "QpwL5tke4Pnpja7X4"
    assert result.json() == S(post_login_successful)
    print("\n")
    pprint(result.json())
