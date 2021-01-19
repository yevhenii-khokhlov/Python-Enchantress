import unittest
from unittest.mock import patch
from parameterized import parameterized
from lectures.tests.hen_house.hen_class import HenHouse, ErrorTimesOfYear


class TestHenHouse(unittest.TestCase):

    def setUp(self) -> None:
        # optional method, may be used to initialize hen_house instance
        self.hen_house = HenHouse(12)

    def test_init_with_less_than_min(self):
        # initialize HenHouse with hens_count less than HenHouse.min_hens_accepted
        # make sure error is raised
        with self.assertRaises(ValueError):
            HenHouse(4)

    @parameterized.expand([(1, "winter"),
                           (3, "spring"),
                           (6, "summer"),
                           (9, "autumn")
                           ])
    def test_season(self, month, season):
        # mock the datetime method/attribute which returns month number
        # make sure correct month ("winter"/"spring" etc.) is returned from season method
        # try to return different seasons
        with patch('datetime.datetime') as datetime_mock:
            datetime_mock.today.return_value.month = month
            self.assertEqual(self.hen_house.season, season)

    def test_productivity_index(self):
        # mock the season method return with some correct season
        # make sure _productivity_index returns correct value based on season and HenHouse.hens_productivity attribute
        with patch.object(HenHouse, 'season', 'summer'):
            self.assertEqual(self.hen_house._productivity_index(), 1)

    def test_productivity_index_incorrect_season(self):
        # mock the season method return with some incorrect season
        # make sure ErrorTimesOfYear is raised when _productivity_index called
        with patch.object(HenHouse, 'season', 'BUG'):
            self.assertRaises(ErrorTimesOfYear, lambda: self.hen_house._productivity_index())

    def test_get_eggs_daily_in_winter(self):
        # test get_eggs_daily function
        # _productivity_index method or season should be mocked
        with patch.object(HenHouse, 'season', 'winter'):
            self.assertEqual(self.hen_house.get_eggs_daily(12), 3)

    def test_get_max_count_for_soup(self):
        # call get_max_count_for_soup with expected_eggs number and check that correct number is returned

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        with patch.object(HenHouse, 'season', 'winter'):
            self.assertEqual(self.hen_house.get_max_count_for_soup(2), 4)

    def test_get_max_count_for_soup_returns_zero(self):
        # call get_max_count_for_soup with expected_eggs number bigger than get_eggs_daily(self.hen_count)
        # zero should be returned.

        # Note: make sure to mock _productivity_index or season
        # in order not to call datetime.datetime.today().month, since it is going to be dynamic value in the future
        with patch.object(HenHouse, 'season', 'winter'):
            self.assertEqual(self.hen_house.get_max_count_for_soup(10), 0)

    def test_food_price(self):
        # mock requests.get and make the result has status_code attr 200 and text to some needed value
        # make sure food-price() return will be of int type
        with patch('hen_class.requests.get') as request_mock:
            request_mock.return_value.status_code = 200
            request_mock.return_value.text = '1' * 11
            self.assertEqual(HenHouse.food_price(), 1)

    def test_food_price_connection_error(self):
        # mock requests.get and make the result has status_code attr not 200
        # check that ConnectionError is raised when food_price method called
        with patch('hen_class.requests.get') as request_mock:
            bad_response = False
            request_mock.return_value.status_code = bad_response
            self.assertRaises(ConnectionError, lambda: self.hen_house.food_price())


if __name__ == '__main__':
    unittest.main()
