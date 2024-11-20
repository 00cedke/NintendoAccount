from flask import Flask, Response, Blueprint
import xml.etree.ElementTree as ET

print("NNAS Started.")

nnas_bp = Blueprint('nnas_protocol', __name__, subdomain='account')