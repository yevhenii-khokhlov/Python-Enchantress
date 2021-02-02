Implement python CRUD functions for shop database and cover it with
integration tests (database connection included) positive and negative
cases (good luck :)

Tests should be in separate module.

# you Should create and test next functions
* `create_user function(dict: user_info)`
* `read_user_info(int: _id)`
* `update_user(dict: new_info, int: _id`
* `delete_user(int: _id)`
* CRUD for cart and cart details should be done together
  `create_cart(dict: cart)` where cart
  `{'user_id': 1, 'creation_time': datetime(...), 'cart_details': [DICTS_WITH_CART_DETAILS]...}`
