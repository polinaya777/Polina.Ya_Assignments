import requests
import sys

def fetch_report(month, department):
    # Base URL of your Flask app
    base_url = "http://127.0.0.1:5000"
    
    # Making requests to both birthdays and anniversaries endpoints
    birthday_response = requests.get(f"{base_url}/birthdays", params={"month": month, "department": department})
    anniversary_response = requests.get(f"{base_url}/anniversaries", params={"month": month, "department": department})
    
    # Parsing JSON response
    birthdays = birthday_response.json()
    anniversaries = anniversary_response.json()
    
    # Printing the report
    print(f"Report for {department} department for {month.capitalize()} fetched.")
    
    if birthdays['total'] > 0:
        print(f"Total Birthdays: {birthdays['total']}")
        print("Employees:")
        for employee in birthdays['employees']:
            print(f"- {employee['birthday']}, {employee['name']}")
        print("\n")  # Adding a newline for better readability
    
    if anniversaries['total'] > 0:
        print(f"Total Anniversaries: {anniversaries['total']}")
        print("Employees:")
        for employee in anniversaries['employees']:
            print(f"- {employee['hire_date']}, {employee['name']}")
            
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fetch_report.py <month> <department>")
        sys.exit(1)
        
    month = sys.argv[1]
    department = sys.argv[2]
    
    fetch_report(month, department)