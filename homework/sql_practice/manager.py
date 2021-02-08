import psycopg2


class Connection:
    def __enter__(self):
        self.connection = psycopg2.connect(dbname="yevhenii",
                                           user="yevhenii",
                                           password='pass',
                                           host='localhost',
                                           port='5432'
                                           )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        return False


def create_user(user_info: dict):
    with Connection() as cursor:
        cursor.execute("""
                       INSERT INTO users (name, email, registration_time)
                       VALUES (%(name)s, %(email)s, %(registration_time)s)
                       """,
                       user_info)


def read_user_info(_id: int):
    with Connection() as cursor:
        cursor.execute('SELECT * FROM users WHERE id = %s',
                       (_id,))
        user_info = cursor.fetchone()
        return user_info


def update_user(new_info: dict, _id: int):
    with Connection() as cursor:
        cursor.execute(f"""
                       UPDATE users SET name = %(name)s, email = %(email)s, 
                       registration_time = %(registration_time)s WHERE id = {_id}
                       """,
                       new_info)


def delete_user(_id: int):
    with Connection() as cursor:
        cursor.execute('DELETE FROM users WHERE id = %s',
                       (_id,))


def create_cart(cart: dict):
    with Connection() as cursor:
        cursor.execute("""
                       INSERT INTO cart (creation_time, user_id) 
                       VALUES (%(creation_time)s, %(user_id)s)
                       """,
                       cart)
        cursor.executemany("""
                           INSERT INTO cart_details (cart_id, price, product) 
                           VALUES (%(cart_id)s, %(price)s, %(product)s)
                           """,
                           cart["cart_details"])


def update_cart(cart: dict):
    with Connection() as cursor:
        cursor.executemany(f"""UPDATE cart SET creation_time = '{cart["creation_time"]}' 
                           WHERE ser_id = {cart['user_id']}""",
                           cart)
        cursor.executemany(f"""
                           UPDATE cart_details SET price = %(price)s, product = %(product)s
                           WHERE cart_id = %(cart_id)s
                           """,
                           cart["cart_details"], )


def read_cart(_id: int):
    with Connection() as cursor:
        cursor.execute('SELECT * FROM cart_details WHERE cart_id = %s',
                       (_id,))
        cart = cursor.fetchall()
        return cart


def delete_cart(_id: int):
    with Connection() as cursor:
        cursor.execute('DELETE FROM cart_details WHERE cart_id = %s',
                       (_id,))
        cursor.execute('DELETE FROM cart WHERE id = %s',
                       (_id,))


if __name__ == '__main__':
    users_dict = {'user_id': 1, 'name': 'Semen', 'email': 'semen@gmail.com',
                  'registration_time': '2021-02-05 07:21:37', "creation_time": '2021-02-05 07:21:37',
                  'cart_details': [{'cart_id': 1, 'price': 130, 'product': 'sony'}]}

    users_dict_update = {'user_id': 1, 'name': 'Ihor', 'email': 'Ihor@yahoo.com',
                         'registration_time': '2021-02-05 07:21:37', "creation_time": '2021-02-05 07:21:37',
                         'cart_details': [{'cart_id': 1, 'price': 300, 'product': 'milk'}]}

    print(read_user_info(4))
    create_cart(users_dict)
