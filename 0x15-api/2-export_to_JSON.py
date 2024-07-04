#!/usr/bin/python3
"""Gathering data from web using restful api"""
import json
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

    tasks = []
    for todo in employee_todos:
        task = {"task": todo['title'],
                "completed": todo['completed'],
                "username": employee_data['username']}
        tasks.append(task)
    employee_tasks = {employee_id: tasks}

    filename = "{}.json".format(employee_id)
    with open(filename, "w") as json_file:
        json.dump(employee_tasks, json_file)
