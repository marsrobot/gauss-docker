import os
import json
from flask import Flask
from flask import request
import logging

app = Flask(__name__)
logger = logging.getLogger('')

@app.route('/')
def web_index():
    return 'index page', 200

def get_json():
    json_str = request.get_json(force=True)
    logger.info(json_str)
    if isinstance(json_str, str):
        json_obj = json.loads(json_str)
    else:
        json_obj = json_str
    return json_obj

@app.route('/sum', methods=['POST'])
def f_sum():
    js = get_json()
    x = int(float(js['x']))
    y = int(float(js['y']))
    s = x + y
    res = {'sum': s}
    return json.dumps(res), 200


if __name__ == '__main__':
    app.run('0.0.0.0',
            port=80,
            debug=True)
