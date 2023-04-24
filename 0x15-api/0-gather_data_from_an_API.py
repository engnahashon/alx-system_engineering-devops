#!/usr/bin/python3
import sys
import requests

"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

employee_id = sys.argv[1]
user_api_url = "https://jsonplaceholder.typicode.com/users/{}"\
    .format(employee_id)
todos_api_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
    .format(employee_id)

response = requests.get(user_api_url)
employee_data = response.json()

response = requests.get(todos_api_url)
employee_todos = response.json()

total = len(employee_todos)
complete = len([task for task in employee_todos if task["completed"]])

print("Employee {} is done with tasks({}/{})"
      .format(employee_data["name"], complete, total))
for todo in employee_todos:
    if todo["completed"]:
        print("\t{}".format(todo["title"]))
