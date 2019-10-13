#How much money can you save in a year?
#Calculating savings based on hourly income, hours worked and weekly cost of living

#Display a greeting
greeting = "Hello "
name = "User"
print(greeting +  name)

#Set up hourly wage and number of hours worked
hourly_wage = 20
hours_per_week = 40

#calculate weekly income
income_per_week = hourly_wage * hours_per_week

#Set up number of weeks worked in a year
weeks_per_year = 48

#Calculate yearly income
income_per_year = weeks_per_year * income_per_week

#Display income
print(name + "'s yearly income is:")
print(income_per_year)

#Set up weekly spending and calculate yearly spendings
spend_per_week = 400
spend_per_year = spend_per_week * 52
print(name + "'s yearly spend is:")
print(spend_per_year)

# --- Calculate the yearly savings ---
savings_per_year = income_per_year - spend_per_year
print(name + "'s yearly savings:")
print(savings_per_year)
