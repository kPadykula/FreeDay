This is simple package to download information about free days.
Package use api from date.nager.at

get_country_code -> return country code based on country name
get_country_name -> return country name based on country code

get_correct_code -> return correct syntax of code
get_correct_country_name -> return correct syntax of name

get_json_free_day_by_code -> return full json file based on country code and year
get_json_free_day_by_name -> return full json file based on country name and year

get_json_available_countries -> return full json file with available countries names and codes

nearest_free_day -> return nearest free day based on country name or code
*nearest_free_day_by_date -> return nearest free day based on country name, code and date
*nearest_free_day_before_date -> return nearest free day before this date based on country name, code and date

furthest_free_day -> return furthest free day i this year based on country code or name
*furthest_free_day_by_date -> return furthest free day in input date based on country code, name and date

get_correct_date -> return correct data

*If you want to use one of above functions you have to remember about date format it have to be string and have this format "yyyy-mm-dd"