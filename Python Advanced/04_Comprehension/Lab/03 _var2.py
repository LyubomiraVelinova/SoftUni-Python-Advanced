countries = input().split(", ")
capitals = input().split(", ")

country_capital_dict = {countries[i]: capitals[i] for i in range(len(countries))}
printing = [print(f"{key} -> {value}") for key, value in country_capital_dict.items()]

# countries = input().split(", ")
# capitals = input().split(", ")
#
# dict = {}
# for i in range(len(countries)):
#     dict[countries[i]] = capitals[i]
#
# for key, value in dict.items():
#     print(f"{key} -> {value}")