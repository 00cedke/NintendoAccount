from flask import Blueprint, request, render_template, make_response

devices = Blueprint("devices", "devices")

@devices.route("/@current/status", methods=['GET'])
def status():
    pass