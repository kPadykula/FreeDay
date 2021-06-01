# FreeDay.py
import datetime
import requests as requests


# Return country code based on country name
def get_country_code(country: str):
    code = ""
    country_after = get_correct_country_name(country)
    for out in get_json_available_countries():
        if out['value'] == country_after:
            code = out['key']
    if code:
        return code
    else:
        return None


# Return country name based on country code
def get_country_name(code: str):
    country = ""
    code_after = get_correct_code(code)
    for out in get_json_available_countries():
        if out['key'] == code_after:
            country = out['value']
    if country:
        return country
    else:
        return None


# correct syntax of code
def get_correct_code(code: str):
    code = code.upper()
    return code


# correct syntax of country name
def get_correct_country_name(country: str):
    country = country.capitalize()
    return country


# get json by code
def get_json_free_day_by_code(code: str, year: int):
    if year > 0:
        response = requests.get("https://date.nager.at/api/v3/publicholidays/{}/{}".format(year, code))
        return response.json()
    else:
        return None


# get json by country name
def get_json_free_day_by_name(country: str, year: int):
    code = get_country_code(country)
    if int(year) > 0:
        response = requests.get("https://date.nager.at/api/v3/publicholidays/{}/{}".format(year, code))
        return response.json()
    else:
        return None


# get json available countries
def get_json_available_countries():
    response = requests.get("https://date.nager.at/api/v2/AvailableCountries")
    return response.json()


# get nearest free day
def nearest_free_day(code_or_country_name: str):
    if len(code_or_country_name) > 2:
        code = get_country_code(code_or_country_name)
    else:
        code = get_correct_code(code_or_country_name)

    current_data = datetime.datetime.today().strftime('%Y-%m-%d')
    current_data_year = datetime.datetime.today().strftime('%Y')
    response = get_json_free_day_by_code(code, int(current_data_year))
    for date in response:
        if date['date'] >= current_data:
            return date['localName'], date['name'], date['date']


# get nearest free day by date
def nearest_free_day_by_date(code_or_country_name: str, date: str):
    if len(code_or_country_name) > 2:
        code = get_country_code(code_or_country_name)
    else:
        code = get_correct_code(code_or_country_name)

    correct_date = get_correct_date(date)
    year = int(correct_date[1])
    response = get_json_free_day_by_code(code, year)
    for date in response:
        if date['date'] >= correct_date[0]:
            return date['localName'], date['name'], date['date']


# get nearest free day before date
def nearest_free_day_before_date(code_or_country_name: str, date: str):
    if len(code_or_country_name) > 2:
        code = get_country_code(code_or_country_name)
    else:
        code = get_correct_code(code_or_country_name)

    correct_date = get_correct_date(date)
    year = int(correct_date[1])
    response = get_json_free_day_by_code(code, year)
    date_return = ""
    for i, date in enumerate(response):
        if i == 0:
            date_return = date
        if date['date'] <= correct_date[0]:
            date_return = date
        if date['date'] >= correct_date[0]:
            return date_return['localName'], date_return['name'], date_return['date']


# get furthest free day in this year
def furthest_free_day(code_or_country_name: str):
    if len(code_or_country_name) > 2:
        code = get_country_code(code_or_country_name)
    else:
        code = get_correct_code(code_or_country_name)

    current_data_year = datetime.datetime.today().strftime('%Y')
    response = get_json_free_day_by_code(code, int(current_data_year))
    for i, date in enumerate(response):
        if date == response[-1]:
            return date['localName'], date['name'], date['date']


# get furthest free day by date
def furthest_free_day_by_date(code_or_country_name: str, date: str):
    if len(code_or_country_name) > 2:
        code = get_country_code(code_or_country_name)
    else:
        code = get_correct_code(code_or_country_name)

    correct_date = get_correct_date(date)
    year = int(correct_date[1])
    response = get_json_free_day_by_code(code, year)
    for i, date in enumerate(response):
        if date == response[-1]:
            return date['localName'], date['name'], date['date']


# return correct date you have to use this format yyyy-mm-dd
def get_correct_date(date: str):
    send = datetime.datetime.strptime(date, '%Y-%m-%d')
    return send.strftime('%Y-%m-%d'), send.strftime('%Y')