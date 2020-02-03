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
    username = user.get('username')

    for task in TODO:
        dtask = {}
        dtask['task'] = task.get('title')
        dtask['completed'] = task.get('completed')
        dtask['username'] = username
        all_tasks.append(dtask)

    jdata = {}
    jdata[ID] = all_tasks

    with open("{}.json".format(ID), 'w') as jf:
        json.dump(jdata, jf)
