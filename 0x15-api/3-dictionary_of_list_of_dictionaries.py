#!/usr/bin/python3
"""
    Python script using this REST API, for a given employee ID, returns
    information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        Using the REST API, for a given employee ID returns information about
        his/her TODO list progress.
        Exporting in a JSON format
    """
    users = requests.get("https://jsonplaceholder.typicode.com/users/",
                         verify=False).json()
    TODO = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    d_users = {}
    d_username = {}

    for user in users:
        ID = user.get('id')
        d_users[ID] = []
        d_username[ID] = user.get('username')

    for task in TODO:
        dtask = {}
        ID = user.get('userId')
        dtask['task'] = task.get('title')
        dtask['completed'] = task.get('completed')
        dtask['username'] = d_username.get(ID)
        d_users.get(ID).append(dtask)

    with open("todo_all_employees.json", 'w') as jf:
        json.dump(d_users, jf)
