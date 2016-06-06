#!/usr/bin/env python

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/msgs", methods=["POST"])
def receive_msg():
    for msg in request.form["msgs"]:
        pass
    return jsonify(error=None), 200


if __name__ == "__main__":
    app.run()
