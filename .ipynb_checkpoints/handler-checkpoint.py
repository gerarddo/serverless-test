import json
import os

from flask import Flask, jsonify, request
app = Flask(__name__)

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

@app.route("/users/<string:user_id>")
def get_user(user_id):

    return jsonify({
        'userId': 'HEY',
        'name': 'ho'
    })