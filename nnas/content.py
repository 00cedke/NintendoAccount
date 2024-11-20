from flask import Flask, request, Response
import xml.etree.ElementTree as ET
import json
import datetime

app = Flask(__name__)

with open('agreements.json', 'r') as f:
    agreements = json.load(f)

@app.route('/agreements/<agreement_type>/<region>/<version>', methods=['GET'])
def agreements_endpoint(agreement_type, region, version):
    response = Response()
    response.headers['Content-Type'] = 'text/xml'
    response.headers['Server'] = 'Nintendo 3DS (http)'
    response.headers['X-Nintendo-Date'] = str(int(datetime.datetime.now().timestamp()))

    root = ET.Element('agreements')
    for agreement in agreements:
        agreement_element = ET.SubElement(root, 'agreement')
        for key, value in agreement.items():
            if isinstance(value, dict):
                texts_element = ET.SubElement(agreement_element, 'texts')
                for sub_key, sub_value in value.items():
                    sub_element = ET.SubElement(texts_element, sub_key)
                    if '#cdata' in sub_value:
                        sub_element.text = sub_value['#cdata']
                    else:
                        sub_element.attrib.update(sub_value)
            else:
                sub_element = ET.SubElement(agreement_element, key)
                sub_element.text = str(value)

    agreements_xml = ET.tostring(root, encoding='utf8', method='xml')
    response.set_data(agreements_xml)
    return response

with open('timezones.json', 'r') as f: 
    timezones = json.load(f)

@app.route('/time_zones/<country_code>/<language>', methods=['GET'])
def time_zones(country_code, language):
    response = Response()
    response.headers['Content-Type'] = 'text/xml'
    response.headers['Server'] = 'Nintendo 3DS (http)'
    response.headers['X-Nintendo-Date'] = str(int(datetime.datetime.now().timestamp()))

    region_languages = timezones[country_code]
    region_timezones = region_languages.get(language, list(region_languages.values())[0])

    timezones_element = ET.Element('timezones')
    for tz in region_timezones:
        timezone_element = ET.SubElement(timezones_element, 'timezone')
        for key, value in tz.items():
            sub_element = ET.SubElement(timezone_element, key)
            sub_element.text = str(value)

    timezones_xml = ET.tostring(timezones_element, encoding='utf8', method='xml')
    response.set_data(timezones_xml)

    return response