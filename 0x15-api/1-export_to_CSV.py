#!/usr/bin/python3
"""
    Python script using this REST API, for a given employee ID, returns
    information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """
        Using the REST API, for a given employee ID returns information about
        his/her TODO list progress.
        Exporting data in CSV
    """
    ID = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    TODO = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()

    with open("{}.csv".format(ID), 'w') as f:
        fill = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in TODO:
            fill.writerow([ID, user.get('username'),
                           task.get('completed'), task.get('title')])
