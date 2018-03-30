from pymystem3 import Mystem
from flask import Flask, request, Response
import json

app = Flask("POS")
m = Mystem()

@app.route('/')
def index(): 
    return '''<h1 id="basedonmystem">Based on MyStem</h1>

<p>POS tagging for Russian language for NetCracker Inc. based on MyStem.</p>

<h2 id="requirements">Requirements</h2>

<p>Install all dependencies via <code>pip3 install -r requirements.txt</code> or just use Dockerfile to create Docker image.</p>

<h2 id="docker">Docker</h2>

<pre><code class="bash language-bash">docker build -t pos-tagger .
docker run -d -it -p 9000:9000 --rm --name pos pos-tagger
</code></pre>

<h2 id="usage">Usage</h2>

<ul>
<li>Service runs on port 9000. </li>

<li>To get POS tag for each word of your sentence, just execute the query <code>/pos/?text=YOURTEXT</code></li>
</ul>'''

@app.route('/pos/')
def pos_tagging():
    string = request.args.get('text')
    
    response = {}
    if string is not None:
        response['tokens'] = m.analyze(string)[:-1]
        return Response(json.dumps(response,ensure_ascii=False, indent = 1), mimetype='application/json')
    else:
        return '''<ul>
<li>To get POS tag for each word of your sentence, just execute the query <code>/pos/?text=YOURTEXT</code></li>
<li>Example of query: /pos/?text=Мама мыла раму</li>
</ul>'''

app.run(host = '0.0.0.0', port = 9000)