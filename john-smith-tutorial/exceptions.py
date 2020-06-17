try:
    age=int(input('Age:'))
    income = 200
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("invalid value")
except ValueError:
    print("invalid value")
