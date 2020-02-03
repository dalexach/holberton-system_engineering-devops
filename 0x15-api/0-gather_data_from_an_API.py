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
    """
    ID = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    TODO = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    all_tasks = []

    for task in TODO:
        # if (task.get('completed') is True) and (ID == task.get('id')):
        if task.get('completed') is True:
            all_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
                                                          len(all_tasks),
                                                          len(TODO)))
    for task in all_tasks:
        print("\t {}".format(task))
