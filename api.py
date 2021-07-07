import json
import os
import authorizer
from flask import Flask, jsonify, request
app = Flask(__name__)

# Endpoint just to check localhost is working
@app.route("/")
def hello():
    return "Hello World! Serverless is up and running."

# Public endpoint will return information to any client
@app.route("/api/public")
def myPublicEndpoint():

    return jsonify({
        'message': 'This is a public API, you can access my secrets...',
        'secrets': 'Pineapple on pizza is actually good for your health.'
    })

# Private endpoint will return information to requests with valid authorization credentials
# Authorization scheme being used is BASIC
# Auth header example: Basic gmijares@lapsusdev.com:ThisIsASecurePassword
@app.route("/api/private")
def myPrivateEndpoint():

    auth = request.headers.get('Authorization').replace('Basic ', '')

    # This response will be unchanged and sent in case Auth Header is not valid
    responseBody = {
        'message' : 'This is a private API, you cannot access my secrets without valid authorization.',
        'secrets' : 'Oops.'
    }

    # Authorizer will return true if Auth Header is valid
    if authorizer.main(auth):

        # Reveal information since auth was valid
        responseBody['message'] = 'This is a private API, you may access my secrets with valid authorization.'
        responseBody['secrets'] = 'Pineapple on pizza is actually good for your health. Mushrooms too.'

    return responseBody

