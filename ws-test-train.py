from flask import Flask, request, abort, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/test-deploy', methods=['POST'])
def test_deploy():
    msg = request.json.get('msg')
    return jsonify(msg)
