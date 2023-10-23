#!/usr/bin/python3
"""Script to fetch employee TODO list"""

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

    emp_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, num_completed_tasks, total_tasks
    ))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
