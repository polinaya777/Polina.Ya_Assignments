import csv
import random
from faker import Faker

fake = Faker()

departments = ["HR", "Finance", "Engineering", "R&D"]
employees = []

for _ in range(1000):  # generate data for 1000 employees
    name = fake.name()
    hire_date = fake.date_between(start_date='-30y', end_date='today')
    department = random.choice(departments)
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=60)

    employees.append({
        "name": name,
        "hire_date": hire_date.strftime('%Y-%m-%d'),
        "department": department,
        "birthday": birthday.strftime('%Y-%m-%d')
    })

with open('database.csv', 'w', newline='') as csvfile:
    fieldnames = ["name", "hire_date", "department", "birthday"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(employees)