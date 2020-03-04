# -*- coding: utf-8 -*-

import requests

#SERVER = "http://localhost:5000"
SERVER = "http://192.168.0.7:5000"

if __name__ == "__main__":
    while True:
        utterance = input()
        if utterance == "\q":
            break
        if utterance == "":
            continue
        requests.post(SERVER, files={"utterance": (None, utterance)})