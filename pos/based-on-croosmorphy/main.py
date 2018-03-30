import subprocess
import json
from flask import Flask, request, Response

from utils import preprocess

app = Flask('POS')
command = lambda x: 'cd /CrossMorphy/bin && ./CrossMorphy --input <(echo {}) --err err.txt'.format(x)

@app.route('/')
def index(): 
    return 'POS tagging for Russian language for NetCracker Inc.'

@app.route('/pos/')
def pos_tagging():
    string = request.args.get('text')

    lexeme = request.args.get('lexeme', None)

    process = subprocess.Popen(command(string), shell=True, executable='/bin/bash', stdout=subprocess.PIPE)
    out = process.communicate()[0].decode("utf-8").split('\n')[:-1]
    process.kill()

    try:
        response = preprocess(out, lexeme)
    except:
        return Response()
    else:
        return Response(response, mimetype='application/json')

app.run(host = '0.0.0.0', port = 9000)
