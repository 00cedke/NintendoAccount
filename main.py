from flask import Flask, Response
import xml.etree.ElementTree as ET

# from conntest import conntest
from nnas import nnas

app = Flask(__name__)

# app.register_blueprint(conntest.conntest)
app.register_blueprint(nnas)

if __name__ == '__main__': 
    app.run(debug=True)