#!/usr/bin/python3
"""Script fetches employee TODO list progress from an API"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    emp_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        emp_id
    )
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        emp_id
    )

    user_res = requests.get(user_url)
    todos_res = requests.get(todos_url)

    if user_res.status_code != 200 or todos_res.status_code != 200:
        print("Failed to retrieve data for employee ID: {}".format(
            emp_id
        ))
        exit(1)

    user_data = user_res.json()
    todos_data = todos_res.json()

    username = user_data.get('username')
    filename = "{}.json".format(emp_id)

    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })

    with open(filename, 'w') as file:
        json.dump({emp_id: tasks_list}, file)
