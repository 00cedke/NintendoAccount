from flask import Flask, Response, Blueprint
import xml.etree.ElementTree as ET

print("NNAS Protocol Started.")

nnas = Blueprint("nnas_protocol", "nnas_protocol")