import datetime
import unittest
from unittest import TestCase
from main import *

dict_for_tests_1 = {
              'user_id': 1,
              'name': 'TestName1',
              'email': 'test1@gmail.com',
              'registration_time': '2021-02-09 08:50:00',
              "creation_time": '2021-02-09 08:50:00',
              'cart_details': [{'cart_id': 1, 'price': 50, 'product': 'android'}]
              }
dict_for_tests_2 = {
              'user_id': 2,
              'name': 'TestName2',
              'email': 'test2@gmail.com',
              'registration_time': '2021-02-09 09:00:00',
              "creation_time": '2021-02-09 09:00:00',
              'cart_details': [{'cart_id': 2, 'price': 100, 'product': 'apple'}]
             }


class MainTest(TestCase):
    def setUp(self) -> None:
        create_user(dict_for_tests_1)
        create_cart(dict_for_tests_1)

    def tearDown(self) -> None:
        with Connection() as cursor:
            cursor.execute("""DELETE FROM cart_details WHERE id>0""")
            cursor.execute("""ALTER SEQUENCE cart_details_id_seq RESTART WITH 1""")
            cursor.execute("""DELETE FROM cart WHERE id>0""")
            cursor.execute("""ALTER SEQUENCE cart_id_seq RESTART WITH 1""")
            cursor.execute("""DELETE FROM users WHERE id>0""")
            cursor.execute("""ALTER SEQUENCE users_id_seq RESTART WITH 1""")

    def test_create_user(self):
        pass

    def test_read_user_info(self):
        self.assertEqual(read_user_info(1),
                         (1, 'TestName1', 'test1@gmail.com', datetime.datetime(2021, 2, 9, 8, 50))
                         )

    def test_update_userinfo(self):
        update_user(dict_for_tests_2, 1)
        self.assertEqual(read_user_info(1),
                         (1, 'TestName2', 'test2@gmail.com', datetime.datetime(2021, 2, 9, 9, 0))
                         )

    def test_delete_user(self):
        delete_user(1)
        self.assertEqual(read_user_info(1), None)

    def test_create_cart(self):
        create_user(dict_for_tests_2)
        create_cart(dict_for_tests_2)
        self.assertEqual(read_cart(2), [(2, 2, 100, 'apple')])

    def test_update_cart(self):
        upd_cart = {
                    "user_id": 1,
                    "creation_time": '2021-02-09 08:50:00',
                    "cart_details": [{'cart_id': 1, 'price': 100, 'product': 'apple'}]
                    }
        update_cart(upd_cart)
        self.assertEqual(read_cart(1), [(1, 1, 100, 'apple')])

    def test_read_cart(self):
        self.assertEqual(read_cart(1), [(1, 1, 50, 'android')])

    def test_delete_cart(self):
        delete_cart(1)
        self.assertEqual(read_cart(1), [])


if __name__ == "__main__":
    unittest.main()
