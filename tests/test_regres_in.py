from pytest_voluptuous import S
from schemas.user import add_user
from schemas.user import users_list_schema
from schemas.user import update_user


def test_update_info_about_user_ok(reqres):
    body = {
        "name": "Alex",
        "job": "lead"
    }
    response = reqres.patch('/api/users/2', data=body)
    assert response.status_code == 200
    assert S(update_user) == response.json()
    assert response.json()["name"] == "Alex"
    assert response.json()["job"] == "lead"


def test_update_info_about_user_when_two_user_job(reqres):
    body = {
        "name": "Alex",
        "job": ["lead", "consalt"]
    }
    response = reqres.patch('/api/users/2', data=body)
    assert response.status_code == 200
    assert response.json()["job"] == ["lead", "consalt"]


def test_get_list_users_ok(reqres):
    response = reqres.get('/api/users', params={"page": 2})

    assert response.status_code == 200
    assert S(users_list_schema) == response.json()
    assert response.json()["data"][0]["email"] == "michael.lawson@reqres.in"


def test_create_user_ok(reqres):
    body = {
        "name": "Alex",
        "job": "lead"
    }
    response = reqres.post('/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()
    assert response.json()["name"] == "Alex"
    assert response.json()["job"] == "lead"


def test_create_user_without_job(reqres):
    body = {
        "name": "Alex"
    }
    response = reqres.post('/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()
