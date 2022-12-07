countries = input().split(", ")
capitals = input().split(", ")

country_capital = list(zip(countries, capitals))
country_capital_dict = {print(f"{key} -> {value}") for (key, value) in country_capital}