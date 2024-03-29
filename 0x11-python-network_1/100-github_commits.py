#!/usr/bin/python3
""" Github code challenge"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
          .format(argv[2], argv[1])
    r = requests.get(url)
    n = 0
    for j in r.json():
        if n < 10:
            print("{}: {}".format(j.get("sha"),
                  j.get("commit").get("author").get("name")))
        n += 1
