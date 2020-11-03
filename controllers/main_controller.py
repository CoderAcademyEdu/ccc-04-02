from flask import Blueprint, request, abort, jsonify
import socket

main = Blueprint('main', __name__, url_prefix="")

count = 0

@main.route("/", methods=["GET"])
def index():
    global count 
    count += 1
    return f"""
    <h1>Server IP is {socket.gethostbyname(socket.gethostname())}</h1>
    <p>Current view count is {count}</p>
    """