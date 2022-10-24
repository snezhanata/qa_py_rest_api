import requests
from pprint import pprint
from pytest_voluptuous import S
from requests import Response

from schemas.schemas import patch_update_job
from tests.test_post_create_user import test_create_user
from utils.base_session import reqres_session

test_create_user()


def test_patch_update_job():
    name = "morpheus"
    job = "zion resident"

    result: Response = reqres_session().patch(
        url="/api/users/2", json={"name": name, "job": job}
    )

    assert result.status_code == 200
    assert result.json()["name"] == "morpheus"
    assert result.json()["job"] == "zion resident"
    assert isinstance(result.json()["updatedAt"], str)
    assert result.json() == S(patch_update_job)
    print("\n")
    pprint(result.json())
