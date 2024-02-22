from flask import Flask, request

import json
import base64
import uuid
import os
import recognition

app = Flask(__name__)

WORKING_DIR = "./working/"
@app.route("/detect_objects", methods = ['POST'])
def detect_objects():
    pic_data = request.get_json()
    format = pic_data["format"]
    base64_data = pic_data["binData"]
    file_path = os.path.join(WORKING_DIR, f"{uuid.uuid4()}.{format}")
    with open(file_path, "wb") as temp_file:
        temp_file.write(base64.b64decode(base64_data))

    result = recognition.detect_objects(file_path)
    os.remove(file_path)

    return [result[0], result[1], result[2]]

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=80)