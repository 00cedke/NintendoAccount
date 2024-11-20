from flask import Flask, Response
import xml.etree.ElementTree as ET

from nnas import nnas
from conntest import conntest

app = Flask(__name__)

app.register_blueprint(conntest)
app.register_blueprint(nnas)

if __name__ == '__main__': 
    app.run(debug=True)