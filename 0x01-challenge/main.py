#!/usr/bin/python3
""" Check response
"""
import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get('http://0.0.0.0:5000/api/v1/status')
        if r.status_code != 200:
            print("Wrong status code: {}".format(r.status_code))
            exit(1)

        if r.headers.get('content-type') != "application/json":
            print("Wrong content type: {}".format(r.headers.get('content-type')))
            exit(1)

        r_json = r.json()

        if len(r_json.keys()) != 1:
            print("Not the right number of element in the JSON: {}".format(r_json))
            exit(1)

        r_status = r_json.get('status')
        if r_status is None:
            print("Missing status key: {}".format(r_json))
            exit(1)

        if r_status != "OK":
            print("Wrong status value: {}".format(r_status))
            exit(1)

        print("OK", end="")
    except:
        print("Error: {}".format(sys.exc_info()))
