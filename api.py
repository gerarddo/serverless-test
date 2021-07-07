import json
import os
import base64 
from flask import Flask, jsonify, request
app = Flask(__name__)

myPersistentAuth = 'gmijares@lapsusdev.com:ThisIsASecurePassword'
authInBytes = myPersistentAuth.encode('ascii')
base64Bytes = base64.b64encode(authInBytes)
base64Auth = base64Bytes.decode('ascii')

@app.route("/")
def hello():
    return "Hello World! Serverless is up and running."

@app.route("/api/public")
def myPublicEndpoint():

    return jsonify({
        'message': 'This is a public API, you can access my secrets...',
        'secrets': 'Pineapple on pizza is actually good for your health.'
    })

@app.route("/api/private")
def myPrivateEndpoint():

    auth = request.headers.get('Authorization').replace('Basic ', '')

    responseBody = {
        'message' : 'This is a private API, you cannot access my secrets without valid authorization.',
        'secrets' : 'Oops.'
    }

    if auth == base64Auth:

        responseBody['message'] = 'This is a private API, you may access my secrets with valid authorization.'
        responseBody['secrets'] = 'Pineapple on pizza is actually good for your health. Mushrooms too.'

    return responseBody

