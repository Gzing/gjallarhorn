from chalice import Chalice

import os
import sendgrid
from sendgrid.helpers.mail import *
import tldextract

app = Chalice(app_name='gjallarhorn')


@app.route('/', methods=['GET'], cors=True)
def index():
    req_data = app.current_request.headers
    referer = req_data.get('referer')
    if referer:
        extract = '.'.join(tldextract.extract(referer)[1:])
        if extract not in os.environ['WHITELIST_DOMAINS'].split(','):
            try:
                sg = sendgrid.SendGridAPIClient(apikey=os.environ['SENDGRID_KEY'])
                from_email = Email(os.environ['FROM_EMAIL'])
                to_email = Email(os.environ['TO_EMAIL'])
                subject = os.environ['EMAIL_SUBJECT']
                content = Content("text/plain", str(app.current_request.headers))
                mail = Mail(from_email, subject, to_email, content)
                sg.client.mail.send.post(request_body=mail.get())
            except Exception as e:
                app.log.error(e)
    return {"img": "not found"}
