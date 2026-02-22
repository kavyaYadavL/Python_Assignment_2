try:
    birth_year = int(input("Enter your birth year: "))

    current_year = 2026
    age = current_year - birth_year

    # Basic calculations
    age_in_months = age * 12
    age_in_days = age * 365
    age_in_hours = age_in_days * 24
    age_in_minutes = age_in_hours * 60
    years_left_100 = 100 - age

    print("Your current age is:", age)
    print("Age in months:", age_in_months)
    print("Age in days:", age_in_days)
    print("Age in hours:", age_in_hours)
    print("Age in minutes:", age_in_minutes)
    print("Years left to turn 100:", years_left_100)

except:
    print("Please enter a valid year.")
