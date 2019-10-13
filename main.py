#How much money can you save in a year?
#Calculating savings based on hourly income, hours worked and weekly cost of living

greeting = "Hello "
name = "User"
print(greeting +  name)

hourly_wage = 20
hours_per_week = 40

income_per_week = hourly_wage * hours_per_week

weeks_per_year = 48

income_per_year = weeks_per_year * income_per_week

print(name + "'s yearly income is:")
print(income_per_year)

spend_per_week = 400
spend_per_year = spend_per_week * 52
print(name + "'s yearly spend is:")
print(spend_per_year)
