from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

def filter_employees(file_name, month, department, date_type):
    # Initialize a list to store the filtered employee data
    filtered_employees = []
    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Check both the month and the department
            if (datetime.strptime(row[date_type], '%Y-%m-%d').month == month and
                row['department'] == department):
                    # Simplify the date format for readability in the response
                    date_format = datetime.strptime(row[date_type], '%Y-%m-%d').strftime('%b %d')
                    filtered_employees.append({"id": reader.line_num, "name": row['name'], date_type: date_format})
    return filtered_employees

@app.route('/birthdays')
def birthdays():
    month = request.args.get('month', default=None, type=str)
    department = request.args.get('department', default=None, type=str)
    month_num = datetime.strptime(month, '%B').month if month else None
    employees = filter_employees('database.csv', month_num, department, 'birthday')
    return jsonify(total=len(employees), employees=employees)

@app.route('/anniversaries')
def anniversaries():
    month = request.args.get('month', default=None, type=str)
    department = request.args.get('department', default=None, type=str)
    month_num = datetime.strptime(month, '%B').month if month else None
    employees = filter_employees('database.csv', month_num, department, 'hire_date')
    return jsonify(total=len(employees), employees=employees)

if __name__ == '__main__':
    app.run(debug=True)