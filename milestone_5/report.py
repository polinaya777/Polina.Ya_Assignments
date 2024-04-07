import csv
import sys
from datetime import datetime

def generate_report(file_name, month, verbose=False):
    departments = ["HR", "Finance", "Engineering", "R&D"]
    birthdays = {department: 0 for department in departments}
    anniversaries = {department: 0 for department in departments}

    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if datetime.strptime(row['birthday'], '%Y-%m-%d').month == month:
                birthdays[row['department']] += 1
                if verbose:
                    print(f"Birthday: {row['name']}")
            if datetime.strptime(row['hire_date'], '%Y-%m-%d').month == month:
                anniversaries[row['department']] += 1
                if verbose:
                    print(f"Anniversary: {row['name']}")

    print(f"--- Birthdays ---\nTotal: {sum(birthdays.values())}")
    for department, count in birthdays.items():
        print(f"- {department}: {count}")

    print(f"--- Anniversaries ---\nTotal: {sum(anniversaries.values())}")
    for department, count in anniversaries.items():
        print(f"- {department}: {count}")

month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 
               7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

if __name__ == "__main__":
    month = datetime.strptime(sys.argv[2], '%B').month
    verbose = '-v' in sys.argv
    print(f"Report for {month_names[month]} generated")
    generate_report(sys.argv[1], month, verbose)