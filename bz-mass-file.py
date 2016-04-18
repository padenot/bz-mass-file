#!/usr/bin/env python3

import sys
import pprint
import requests

INSTANCE='https://bugzilla.mozilla.org/'

def open_bugs(bugs):
    key = trim(file.open("key.txt").readlines()[0])
    params = {
      "api_key": key,
      "product" : "Core",
      "component" : "Web Audio",
      "summary" : "",
      "description": "",
      "status": "NEW",
      "version": "Trunk"
    }

    def format(description, link):
        return description + "\n\n" + "Spec changes at " + link + "."

    for bug in bugs:
        description_with_link = format(bug["description"], bug["link"])
        params["summary"] = bug["summary"]
        params["description"] = description_with_link
        r = requests.post(INSTANCE + '/rest/bug', params=params)
        print(r.text)

def parse(file_name):
    bugs = []
    lines = open(file_name).readlines()

    def to_link(string):
        if string[0:4] == "http":
            return string
        else:
            return "https://github.com/webaudio/web-audio-api/commit/" + string

    def trim(string):
        return string[0:-1]


    i = 0
    while i < len(lines):
        d = {}
        d["link"] = to_link(trim(lines[i]))
        i = i+1
        d["summary"] = trim(lines[i])
        i = i+1
        d["description"] = trim(lines[i])
        i = i+1
        if len(lines) != i and lines[i] != "\n":
            print("formatting error at line " + str(i))
            print(lines[i])
            sys.exit(1)
        i = i+1

        bugs.append(d)

    return bugs

open_bugs(parse("bugs.txt"))
