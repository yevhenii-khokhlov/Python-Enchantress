import pytest
from freezegun import freeze_time
from .Amazon_killer import amazon_killer as app

FROZEN_TIME = '2021-02-19T11:45:00'


@pytest.fixture
def store_app():
    app.config['TESTING'] = True
    with app.test_client() as client:
        return client


@freeze_time(FROZEN_TIME)
def test_users_methods(store_app):

    # POST method testing
    response = store_app.post('/users')
    assert response.status_code == 201
    assert response.json == {
        "user_id": 1,
        "registration_timestamp": FROZEN_TIME
    }

    # GET method testing
    user_id = response.json['user_id']
    response = store_app.get(f'/users/{user_id}')
    assert response.status_code == 200
    assert response.json == {
        "user_id": user_id,
        "registration_timestamp": FROZEN_TIME,
    }

    # PUT method testing
    response = store_app.put(
        f"/users/1",
        json={
            "name": "Yevhenii",
            "email": "test@test.com"
        }
    )
    assert response.status_code == 201
    assert response.json == {"status": "success"}

    # DELETE method testing
    response = store_app.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json == {"status": "success"}


@freeze_time(FROZEN_TIME)
def test_carts_methods(store_app):

    # POST method testing
    response = store_app.post(
        "/carts",
        json={
            "user_id": 1,
            "products": [
                {
                    "product": "bread",
                    "price": 25,
                },
                {
                    "product": "butter",
                    "price": 50,
                }
            ]
        }
    )
    assert response.status_code == 201
    assert response.json == {
        "cart_id": 1,
        "registration_timestamp": FROZEN_TIME
    }

    # GET method testing
    cart_id = response.json["cart_id"]
    response = store_app.get(f"/carts/{cart_id}")
    assert response.status_code == 200
    assert response.json == {
        "cart_id": 1,
        "registration_timestamp": FROZEN_TIME,
    }

    # PUT method testing
    response = store_app.put(
        "/carts/1",
        json={
            "user_id": 1,
            "creating_time": FROZEN_TIME,
            "products": [
                {
                    "product": 'bread',
                    "price": 25,
                }
            ]
        }
    )
    assert response.status_code == 200
    assert response.json == {"status": "success"}

    # DELETE method testing
    response = store_app.delete(f"/carts/{cart_id}")
    assert response.status_code == 200
    assert response.json == {"status": "success"}


def test_get_user_no_such_user(store_app):
    response = store_app.get("/users/2")
    assert response.status_code == 404
    assert response.json == {"Error": "no user in base with id 2"}


@freeze_time(FROZEN_TIME)
def test_get_no_such_cart(store_app):
    response = store_app.get("/carts/10")
    assert response.status_code == 404
    assert response.json == {"Error": "no cart in base with id 10"}
