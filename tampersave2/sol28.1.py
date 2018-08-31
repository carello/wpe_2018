#!/usr/bin/env python3.6

from filescan import FileList
from flask import Flask, request
import os
import pickle

app = Flask(__name__)

def pathname_to_picklename(s):
    return s.replace(b'/', b'-')    

@app.route("/scan/")
def scan():
    pathname = request.query_string.decode('utf-8')

    if not os.path.exists(pathname):
        return f"Error: No such path '{pathname}'"
    elif not os.path.isdir(pathname):
        return f"Error: '{pathname}' is not a directory"
    else:
        fl = FileList(pathname)
        pickle_filename = pathname_to_picklename(pathname)
        fl.scan()
        pickle.dump(fl, open(pickle_filename, 'wb'))
        return f"Successfully scanned and pickled."

@app.route('/rescan/')
def rescan():
    pathname = request.query_string

    if not os.path.exists(pathname):
        return f"Error: No such path '{pathname}'"
    elif not os.path.isdir(pathname):
        return f"Error: '{pathname}' is not a directory"
    elif not os.path.exists(pathname_to_picklename(pathname)):
        return f"Error: No record of scanning '{pathname}'"
    else:
        fl = pickle.load(open(pathname_to_picklename(pathname), 'rb'))
        return fl.rescan()

app.run()
