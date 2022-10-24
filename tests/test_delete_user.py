import requests
from requests import Response

from tests.test_post_create_user import test_create_user
from utils.base_session import reqres_session

test_create_user()


def test_delete_user():
    result: Response = reqres_session().delete(url="/api/users/2")
    assert result.status_code == 204
