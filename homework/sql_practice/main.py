import psycopg2

DB_NAME = "yevhenii"
USER = "yevhenii"
PASSWORD = "pass"
HOST = "localhost"
PORT = "5432"


class Connection:
    def __init__(self):
        self.dbname = DB_NAME
        self.user = USER
        self.password = PASSWORD
        self.host = HOST
        self.port = PORT

    def __enter__(self):
        self.connection = psycopg2.connect(
                                           dbname=self.dbname,
                                           user=self.user,
                                           password=self.password,
                                           host=self.host,
                                           port=self.port
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
        delete_cart(_id)
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
                           WHERE user_id = {cart['user_id']}""",
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
    pass
