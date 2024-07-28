To create a Python script that checks the status of subdomains and updates the status in a tabular format every minute, you can use the `requests` library to check the HTTP status and the `tabulate` library to display the results in a table. Additionally, the `time` library can be used to handle the periodic checking.

Here's the complete script:

1. Install necessary libraries:
```bash
pip install requests tabulate
```

2. Create the Python script:
```python
import requests
from tabulate import tabulate
import time

# List of subdomains to check
subdomains = [
    "https://vlearnv.herovired.com/",
    "https://github.com/",
    "https://google.com",
]

def check_status(subdomains):
    status_list = []
    for subdomain in subdomains:
        try:
            response = requests.get(subdomain, timeout=5)
            status = "Up" if response.status_code == 200 else "Down"
        except requests.exceptions.RequestException:
            status = "Down"
        status_list.append((subdomain, status))
    return status_list

def print_status_table(status_list):
    table = tabulate(status_list, headers=["Subdomain", "Status"], tablefmt="grid")
    print(table)

def main():
    while True:
        status_list = check_status(subdomains)
        print("\033c", end="")  # Clear the console
        print_status_table(status_list)
        time.sleep(60)

if __name__ == "__main__":
    main()

```

### Explanation:
1. **List of Subdomains:** Define a list of subdomains that you want to check.
2. **check_status Function:** This function checks the status of each subdomain by making an HTTP GET request. If the request is successful and returns a status code of 200, the subdomain is considered "Up". Any other response or an exception is considered "Down".
3. **print_status_table Function:** This function prints the status of subdomains in a tabular format using the `tabulate` library.
4. **main Function:** This function runs an infinite loop that:
   - Checks the status of subdomains.
   - Clears the console.
   - Prints the status in a table.
   - Waits for 60 seconds before repeating.

### Running the Script
To run the script, simply execute it with Python:
```bash
python check_subdomains.py
```

This script will continuously check the status of the specified subdomains every minute and display the results in a tabular format on the screen.
