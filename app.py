import os

from flask import Flask, request, Response
from flask_cors import CORS
import sendgrid
from sendgrid.helpers.mail import *
import tldextract


app = Flask(__name__)
CORS(app)

BLANK_IMG = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b'


@app.route('/', methods=['GET'])
@app.route('/<filename>', methods=['GET'])
def index(filename=None):
    referer = request.headers.get('referer')
    if referer:
        extract = tldextract.extract(referer)
        extract = extract.fqdn or extract.ipv4
        if extract not in os.environ['WHITELIST_DOMAINS'].split(','):
            try:
                sg = sendgrid.SendGridAPIClient(apikey=os.environ['SENDGRID_KEY'])
                from_email = Email(os.environ['FROM_EMAIL'])
                to_email = Email(os.environ['TO_EMAIL'])
                subject = os.environ['EMAIL_SUBJECT']
                content = Content("text/plain", str(request.headers))
                mail = Mail(from_email, subject, to_email, content)
                sg.client.mail.send.post(request_body=mail.get())
            except Exception as e:
                app.logger.error(e)
    return Response(BLANK_IMG, mimetype='image/gif')
