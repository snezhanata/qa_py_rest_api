from pytest_voluptuous import S
from requests import Response

from schemas.schemas import post_create_user_schema
from utils.base_session import reqres_session


def test_create_user():
    name = "octavio"
    job = "leader"

    result: Response = reqres_session().post(
        url="/api/users", json={"name": name, "job": job}
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(post_create_user_schema)
