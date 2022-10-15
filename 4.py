viewing_years = int(input("годы в течении которых посетитель будет постоянно смотреть на экспонаты"))
print("Кол-во просмотренных экспонатов:", viewing_years * 365 * 8 * 60 // 5)

exhibits = int(input("кол-во красивых экспонатов"))

years = exhibits // 35040
exhibits %= 35040
days = exhibits // 96
exhibits %= 96

print("years", years, "days", days, "mins", exhibits * 5)
