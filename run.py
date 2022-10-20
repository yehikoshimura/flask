from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route("/")
def get_json():
    with open("./json/test.json", "r") as f:
        json_file = json.load(f)

    return json.dumps(json_file, indent=2)


if __name__ == "__main__":
    app.run()
