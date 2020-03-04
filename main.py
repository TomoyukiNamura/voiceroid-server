# -*- coding: utf-8 -*-

import time
from flask import *
import subprocess
from src.voiceroid2 import VoiceRoid2


VOICEROID2_PATH = "C:\Program Files (x86)\AHS\VOICEROID2\VoiceroidEditor.exe"
TIME_LAG = 3

app = Flask(__name__)

# voiceroid2の起動
subprocess.Popen(VOICEROID2_PATH)
time.sleep(TIME_LAG)
vr2 = VoiceRoid2()

while vr2.is_run==False:
    time.sleep(TIME_LAG)
    vr2 = VoiceRoid2()


@app.route("/", methods=["GET", "POST"])
def utterance():
    if request.method == "POST":
        vr2.utterance(str(request.form["utterance"]))
        return "0\n"
    else:
        return "1\n"
        
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)