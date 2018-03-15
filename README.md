# gjallarhorn

Create a python3 virtual env
`virtualenv -p python3 .chalice/env`


Activate the created virtual env
`. .chalice/env/bin/activate`


Install requirements
`pip install -r requirements.txt`


Create a configuration file at .chalice/config.json

```
{
  "version": "2.0",
  "app_name": "gjallarhorn",
  "environment_variables": {
    "WHITELIST_DOMAINS": Domain list split by commas "google.com,yahoo.com,localhost.,127.0.0.1.",
    "FROM_EMAIL": "xyz@example.com",
    "TO_EMAIL": "abc@example.com",
    "SENDGRID_KEY": "sendgrid key",
    "EMAIL_SUBJECT": "Subject of the email"
  },
  "stages": {
    "dev": {
      "api_gateway_stage": "api"
    }
  }
}
```


If this is your first time configuring credentials for AWS you can follow these steps to quickly get started:
```
$ mkdir ~/.aws
$ cat >> ~/.aws/config
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=YOUR_REGION (such as us-west-2, us-west-1, etc)
```


To test locally:
`chalice local`


To deploy on aws:
`chalice deploy`

