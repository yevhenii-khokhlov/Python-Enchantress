import unittest
from unittest.mock import patch


from homework.tests_simple_employee import Employee


class SimpleEmployeeTest(unittest.TestCase):
    """Class for making unittests of 'test_simple_employee.py' """
    first = "Firstname"
    last = "Lastname"
    pay = 4200
    email = "Firstname.Lastname@email.com"
    fullname = "Firstname Lastname"
    raise_amt = Employee.raise_amt

    def setUp(self) -> None:
        self.test_employee = Employee(self.first, self.last, self.pay)

    def test_return_from_email(self):
        self.assertEqual(self.test_employee.email, self.email)

    def test_return_from_fullname(self):
        self.assertEqual(self.test_employee.fullname, self.fullname)

    def test_apply_raise(self):
        self.test_employee.apply_raise()
        self.assertEqual(self.test_employee.pay, self.pay * self.raise_amt)

    def test_return_from_monthly_schedule(self):
        with patch('tests_simple_employee.requests.get') as mock_requests:
            mock_requests.return_value.ok = True
            self.assertNotEqual(self.test_employee.monthly_schedule('june'), 'Bad Response!')


if __name__ == "__main__":
    unittest.main()
