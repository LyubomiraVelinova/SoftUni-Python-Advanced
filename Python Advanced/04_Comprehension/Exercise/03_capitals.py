countries = input().split(", ")
capital_cities = input().split(", ")
print({country: capital for country, capital in list(zip(countries, capital_cities))})
