#!/usr/bin/python3
"""Gathering data from web using restful api"""
import csv
import requests
import sys


if __name__ == "__main__":
    """Python script that, using this REST API, for a given employee ID"""
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

    filename = "{}.csv".format(employee_id)
    with open(filename, mode="w", newline="") as csv_file:
        field = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=field)

        writer.writeheader()
        for todo in employee_todos:
            writer.writerow({"USER_ID": employee_id,
                            "USERNAME": employee_data["username"],
			    "TASK_COMPLETED_STATUS": todo["completed"],
			    "TASK_TITLE": todo["title"]})
