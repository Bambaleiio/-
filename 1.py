name = "Sanek"
second_name = "Kriper"
year = 2010

print(name, second_name, year)

name, second_name = second_name, name
year += 60 # year = year + 60

print(name, second_name, year)