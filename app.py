import json
import sys
from flask import Flask, request
from flask_cors import CORS
import requests
import socket
import netifaces
from urllib.parse import urlencode
app = Flask(__name__)


def after_request(resp):
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    return resp


app.after_request(after_request)
CORS(app)


def returner(code, msg, data):
    return {
        'code': code,
        'msg': msg,
        'data': data
    }


def api(entry, params, color_mark):
    try:
        print("http://{}?{}".format(entry, params))
        print("color_mark:".format(color_mark))
        if color_mark is not None:
            headers = {"X-Nsf-Mark": color_mark}
            response = requests.get("http://{}?{}".format(entry, params), headers=headers)
        else:
            response = requests.get("http://{}?{}".format(entry, params))
    except Exception as e:
        return returner(501, "Exception", str(e))
    return response.content


@app.route('/api', methods=["GET"])
def api_redirect():
    if "entry" in request.args:
        entry = request.args.get("entry")
    else:
        return returner(403, "failed", "[entry] is required")

    if "color_mark" in request.args:
        color_mark = request.args.get("color_mark")
    else:
        color_mark = None
    # color_mark = request.headers.get('X-Nsf-Mark')
    print(request.headers)
    # print(color_mark)
    return api(entry, urlencode(request.args), color_mark)


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8089
    app.run(host='0.0.0.0', port=8089)
