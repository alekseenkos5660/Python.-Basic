# import re
# # Задание 1:
#
# # Создайте класс «Город». Необходимо хранить в полях класса: название города, название региона,
# # название страны, количество жителей в городе, почтовый индекс города, телефонный код города.
# # Реализуйте доступ к отдельным полям через методы класса.
# # get and set (по примеру на уроке)
#
#
# class City:
#     __name_city: str = "no name"
#     __name_region: str = "no name"
#     __name_country: str = "no name"
#     __population: int = 0
#     __postal_code: str = "no postal code"
#     __telephone_code: str = "no telephone code"
#
#     def __init__(self, name_city, name_region, name_country, population, postal_code, telephone_code):
#         self.__name_city = name_city
#         self.__name_region = name_region
#         self.__name_country = name_country
#         self.__population = population
#         self.__postal_code = postal_code
#         self.__telephone_code = telephone_code
#
#     def set_name_city(self, name_city):
#         if re.match(r'^[\sA-Za-z-]{2,25}$', name_city):
#             self.__name_city = name_city
#         else:
#             print("Incorrect city name!")
#
#     def get_name_city(self):
#         return self.__name_city
#
#     def set_name_region(self, name_region):
#         if re.match(r'^[\sA-Za-z-]{2,25}$', name_region):
#             self.__name_region = name_region
#         else:
#             print("Incorrect region name!")
#
#     def get_name_region(self):
#         return self.__name_region
#
#     def set_name_country(self, name_country):
#         if re.match(r'^[\sA-Za-z-]{2,25}$', name_country):
#             self.__name_country = name_country
#         else:
#             print("Incorrect country name!")
#
#     def get_name_country(self):
#         return self.__name_country
#
#     def set_population(self, population):
#         if 100 <= population <= 10000000:
#             self.__population = population
#         else:
#             print("Incorrect population!")
#
#     def get_population(self):
#         return self.__population
#
#     def set_postal_code(self, postal_code):
#         if 4 <= len(postal_code) <= 10:
#             self.__postal_code = postal_code
#         else:
#             print("Incorrect postal code!")
#
#     def get_postal_code(self):
#         return self.__postal_code
#
#     def set_telephone_code(self, telephone_code):
#         if re.match(r'^(\+\d{2,3})?\d{3}$', telephone_code):
#             self.__telephone_code = telephone_code
#         else:
#             print("Incorrect telephone code!")
#
#     def telephone_code(self):
#         return self.__telephone_code
#
#     def show_info(self):
#         print(f"City: {self.__name_city} \nRegion: {self.__name_region}"
#               f"\nCountry: {self.__name_country} \nPopulation: {self.__population}"
#               f"\nPostal code: {self.__postal_code} \nTelephone code: {self.__telephone_code}")
#
#
# Dnipro = City("Dnipro", "Dnipro", "Ukraine", "966400", "49000", "056")
# Dnipro.show_info()
# Dnipro.set_name_city("New York City")
# Dnipro.set_name_region("Mid-Atlantic")
# Dnipro.set_name_country("USA")
# Dnipro.set_population(8468000)
# Dnipro.set_postal_code("11101")
# Dnipro.set_telephone_code("212")
# Dnipro.show_info()
#
# # Задание 2:
#
# # Создайте класс «Страна». Необходимо хранить в полях класса: название страны, название континента,
# # количество жителей в стране, телефонный код страны, название столицы, название городов страны.
# # Реализуйте доступ к отдельным полям через методы класса.
# # get and set (по примеру на уроке)
#
#
# class Country:
#     __name_country: str = "no name"
#     __name_continent: str = "no name"
#     __population: int = 0
#     __telephone_code: str = "no telephone code"
#     __name_capital: str = "no name"
#     __name_city: str = "no name"
#     __postal_code: str = "no postal code"
#
#     def __init__(self, name_country, name_continent, population, telephone_code,
#                  name_capital, name_city, postal_code):
#         self.__name_country = name_country
#         self.__name_continent = name_continent
#         self.__population = population
#         self.__telephone_code = telephone_code
#         self.__name_capital = name_capital
#         self.__name_city = name_city
#         self.__postal_code = postal_code
#
#     def set_name_country(self, name_country):
#         if re.match(r'^[\sA-Za-z-]{2,25}$', name_country):
#             self.__name_country = name_country
#         else:
#             print("Incorrect country name!")
#
#     def get_name_country(self):
#         return self.__name_country
#
#     def set_name_continent(self, name_continent):
#         continents = ["Asia", "Africa", "North America", "South America", "Antarctica", "Europe", "Australia"]
#         if name_continent in continents:
#             self.__name_continent = name_continent
#         else:
#             print("Incorrect continent name!")
#
#     def get_name_continent(self):
#         return self.__name_continent
#
#     def set_population(self, population):
#         if 100 <= population <= 1000000000:
#             self.__population = population
#         else:
#             print("Incorrect population!")
#
#     def set_telephone_code(self, telephone_code):
#         if re.match(r'^\+\d{2,3}$', telephone_code):
#             self.__telephone_code = telephone_code
#         else:
#             print("Incorrect telephone code!")
#
#     def set_name_capital(self, name_capital):
#         if re.match(r'^[\sA-Za-z-]{2,25}$', name_capital):
#             self.__name_capital = name_capital
#         else:
#             print("Incorrect capital name!")
#
#     def get_name_capital(self):
#         return self.__name_capital
#
#     def set_name_city(self, name_city):
#         if re.match(r'^[\sA-Za-z-]{2,25}$', name_city):
#             self.__name_city = name_city
#         else:
#             print("Incorrect city name!")
#
#     def get_name_city(self):
#         return self.__name_city
#
#     def set_postal_code(self, postal_code):
#         if 4 <= len(postal_code) <= 10:
#             self.__postal_code = postal_code
#         else:
#             print("Incorrect postal code!")
#
#     def get_postal_code(self):
#         return self.__postal_code
#
#     def show_info(self):
#         print(f"Country: {self.__name_country} \nContinent: {self.__name_continent}"
#               f"\nPopulation: {self.__population} \nTelephone code: {self.__telephone_code}"
#               f"\nCapital: {self.__name_capital} \nCity: {self.__name_city}"
#               f"\nPostal code: {self.__postal_code}")
#
#
# Ukraine = Country("Ukraine", "Europe", "29000000", "+38", "Kyiv", "Kyiv", "01001")
# Ukraine.show_info()
# Ukraine.set_name_country("Brazil")
# Ukraine.set_name_continent("South America")
# Ukraine.set_population(214300000)
# Ukraine.set_telephone_code("+55")
# Ukraine.set_name_capital("Brasilia")
# Ukraine.set_name_city("Rio de Janeiro")
# Ukraine.set_postal_code("20000-000")
# Ukraine.show_info()
