from flask import Blueprint, Response

print("CONNTEST Started.")

conntest_bp = Blueprint('conntest', __name__, subdomain='conntest')

@conntest_bp.route('/', methods=['GET'])
def conntest():
    response = Response()
    response.headers['Content-Type'] = 'text/html'
    response.headers['X-Organization'] = 'Nintendo'

    html_content = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
    <head>
    <title>HTML Page</title>
    </head>
    <body bgcolor="#FFFFFF">
    This is test.html page
    </body>
    </html>
    """
    response.set_data(html_content)
    return response