#!/usr/bin/python3
""" Get todos from user """
import json
import requests
from sys import argv

if __name__ == "__main__":
    a = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(argv[1])).json()

    b = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1])).json()
    u = b["username"]
    list = []
    for i in a:
        if (((i["userId"]) == int(argv[1]))):
            dict = {}
            dict["task"] = i["title"]
            dict["completed"] = i["completed"]
            dict["username"] = u
            list.append(dict)
    dict_1 = {}
    dict_1[argv[1]] = list
    with open("{}.json".format(argv[1]), 'w') as f:
        json.dump(dict_1, f)
