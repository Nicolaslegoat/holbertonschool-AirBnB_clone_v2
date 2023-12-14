#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host=0.0.0.0, port=5000)
