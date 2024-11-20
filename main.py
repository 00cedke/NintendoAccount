from flask import Flask, Response
import xml.etree.ElementTree as ET

from nnas import protocol

app = Flask(__name__)

app.register_blueprint(protocol)

if __name__ == '__main__': 
    app.run(debug=True)