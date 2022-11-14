#!/usr/bin/python3
import requests
from sys import argv
""" Accessing a url with employee ID """


if __name__ == "__main__":
    """ Get employees todo list """
    list = []
    a = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(argv[1]))
    a = a.json()
    b = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1]))
    b = b.json()
    x = 0
    y = 0
    for i in a:
        if (((i["userId"]) == int(argv[1]))):
            x += 1
            if (i["completed"]):
                y += 1
                list = list + [(i["title"])]
    print("Employee {} is done with tasks({}/{}):".format(
        b["name"], y, x))
    for i in list:
        print("\t", i)
