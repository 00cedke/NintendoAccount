from flask import Flask, Response
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/@current/status', methods=['GET'])
def status():
    device = ET.Element('device')
    device_xml = ET.tostring(device, encoding='utf8', method='xml')
    return Response(device_xml, mimetype='application/xml')