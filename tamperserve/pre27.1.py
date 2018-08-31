from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/scan")
def scan():
    pathname = request.query_string.decode('utf-8')

    if os.path.exists(pathname):
        return str(', '.join(os.listdir(pathname)))
    else:
        return f"No such directory '{pathname}'"

app.run()

