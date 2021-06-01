import unittest
import requests

from FreeDay import FreeDay


class FreeDayTest(unittest.TestCase):

    def test_country_code(self):
        assert FreeDay.get_country_code("Barbados") == "BB"

    def test_country_name(self):
        assert FreeDay.get_country_name("be") == "Belgium"

    def test_correct_code(self):
        assert FreeDay.get_correct_code("pl") == "PL"

    def test_correct_name(self):
        assert FreeDay.get_correct_country_name("poLANd") == "Poland"

    def test_json_by_code(self):
        test_json = requests.get("https://date.nager.at/api/v3/publicholidays/{}/{}".format(2010, "PL"))
        assert FreeDay.get_json_free_day_by_code("pl", 2010) == test_json.json()

    def test_json_by_name(self):
        test_json = requests.get("https://date.nager.at/api/v3/publicholidays/{}/{}".format(2220, "BJ"))
        assert FreeDay.get_json_free_day_by_name("Benin", 2220) == test_json.json()

    def test_json_available_countries(self):
        test_json = requests.get("https://date.nager.at/api/v2/AvailableCountries")
        assert FreeDay.get_json_available_countries() == test_json.json()

    # test in 2021.06.1
    def test_nearest_free_day(self):
        assert FreeDay.nearest_free_day("Australia") == ('Western Australia Day', 'Western Australia Day', "2021-06-07")

    # test in 2021.06.01
    def test_nearest_free_day_code(self):
        assert FreeDay.nearest_free_day("au") == ('Western Australia Day', 'Western Australia Day', "2021-06-07")

    # test in 2021.06.01
    def test_nearest_free_day_by_date(self):
        assert FreeDay.nearest_free_day_by_date("Colombia", "2022-03-15") == (
            'Día de San José', "Saint Joseph's Day", '2022-03-19')

    # test in 2021.06.01
    def test_nearest_free_day_by_date_code(self):
        assert FreeDay.nearest_free_day_by_date("cO", "2022-03-15") == (
            'Día de San José', "Saint Joseph's Day", '2022-03-19')

    # test in 2021.06.01
    def test_nearest_free_day_before_date(self):
        assert FreeDay.nearest_free_day_before_date("frAnce", "2320-01-13") == (
            "Jour de l'an", "New Year's Day", '2320-01-01')

    # test in 2021.06.01
    def test_nearest_free_day_before_date_code(self):
        assert FreeDay.nearest_free_day_before_date("Fr", "2320-01-13") == (
            "Jour de l'an", "New Year's Day", '2320-01-01')

    def test_furthest_free_day(self):
        assert FreeDay.furthest_free_day("GuYaNa") == ('Boxing Day', 'Boxing Day', '2021-12-26')

    def test_furthest_free_day_code(self):
        assert FreeDay.furthest_free_day("GY") == ('Boxing Day', 'Boxing Day', '2021-12-26')

    def test_furthest_free_day_by_date(self):
        assert FreeDay.furthest_free_day_by_date("ICEland", "1100-03-12") == (
            'Gamlársdagur', "New Year's Eve", '1100-12-31')

    def test_furthest_free_day_by_date_code(self):
        assert FreeDay.furthest_free_day_by_date("is", "1100-03-12") == ('Gamlársdagur', "New Year's Eve", '1100-12-31')

    def test_correct_date(self):
        assert FreeDay.get_correct_date("2113-4-4") == ('2113-04-04', '2113')


if "__main__" == __name__:
    unittest.main()