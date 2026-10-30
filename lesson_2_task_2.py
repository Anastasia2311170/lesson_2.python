def is_year_leap(numb):
    return (True) if numb % 4 == 0 else (False)


year = int(input("Введите год: "))
result = is_year_leap(year)
print(f"год:  {year} - {result}")
