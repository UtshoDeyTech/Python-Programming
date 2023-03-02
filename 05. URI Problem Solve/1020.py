age_in_days = int(input())

years = age_in_days // 365
age_in_days -= years * 365

months = age_in_days // 30
age_in_days -= months * 30

days = age_in_days

print(years, 'ano(s)')
print(months, 'mes(es)')
print(days, 'dia(s)')
