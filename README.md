# gjallarhorn

Create a python3 virtual env
`python3.6 -m venv venv/`


Activate the created virtual env
`. ./venv/bin/activate`


Install requirements
`pip install -r requirements.txt`


Set the following environment variables:
```
WHITELIST_DOMAINS (Domain list split by commas "google.com,yahoo.com,localhost,127.0.0.1"),
FROM_EMAIL (e.g. "xyz@example.com")
TO_EMAIL (e.g. "abc@example.com")
SENDGRID_KEY (sendgrid key)
EMAIL_SUBJECT (Subject of the email)
```

To test locally:
`FLASK_APP=app.py flask run`


## Heroku Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Gzing/gjallarhorn/tree/master)
