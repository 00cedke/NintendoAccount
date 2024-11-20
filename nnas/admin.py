from flask import Blueprint, request, render_template, make_response

admin = Blueprint("admin", "admin")

@admin.route("/mapped_ids", methods=['POST'])
def mapped_ids():
    pass