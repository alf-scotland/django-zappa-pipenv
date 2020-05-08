# Example Django + Zappa + pipenv

Example application using Django, Zappa, and pipenv.

## Getting started

To get started update the Zappa configuration (`zappa_settings.json`) if you desire. Then deploy

```bash
zappa deploy dev
```

This example uses `python-dotenv` to configure your django application via environment variables. The last step is to configure the allowed host. Therefore, you need to find out the domain where your lambda function is hosted. This can be achieved by calling `zappa status dev`:

```bash
$ zappa status dev
zappa status dev
Status for example-dev:
        Lambda Versions:      2
        Lambda Name:          example-dev
        Lambda ARN:           arn:aws:lambda:eu-central-1:012345:function:example-dev
        Lambda Role ARN:      arn:aws:iam::012345:role/example-dev-ZappaLambdaExecutionRole
        Lambda Handler:       handler.lambda_handler
        Lambda Code Size:     22113064
        Lambda Version:       $LATEST
        Lambda Last Modified: 2020-05-08T13:08:25.738+0000
        Lambda Memory Size:   512
        Lambda Timeout:       30
        Lambda Runtime:       python3.7
        Lambda VPC ID:        None
        Invocations (24h):    0
        Errors (24h):         0
        Error Rate (24h):     Error calculating
        API Gateway URL:      https://xyz.execute-api.eu-central-1.amazonaws.com/dev
        Domain URL:           None Supplied
        Num. Event Rules:     1
        Event Rule Name:      example-dev-zappa-keep-warm-handler.keep_warm_callback
        Event Rule Schedule:  rate(4 minutes)
        Event Rule State:     Enabled
        Event Rule ARN:       arn:aws:events:eu-central-1:012345:rule/example-dev-zappa-keep-warm-handler.keep_warm_callback
```

Use the `API Gateway URL` domain and set it as an environment variable on the Lambda console for the variable `ALLOWED_HOST`.

**Done!**

## How this project was created

Create a project folder

```bash
mkdir project-name
cd project-name
```

Create a virtual environment and install `django` and `zappa` (`python-dotenv` to manage environment variables):

```bash
pipenv install zappa django python-dotenv
pipenv shell
```

Then start a Django project

```bash
django-admin startproject example .
```

Important, note the `.` at the end to indicate to Django to create files within the directory.

Then create an app:

```bash
python manage.py startapp app
```

And link the app in the config as well as make sure that `python-dotenv` can get to work.

```python
# example/settings.py

from dotenv import load_dotenv  # right after import os
from pathlib import Path

# replace BASE_DIR with
BASE_DIR = Path(__file__).absolute().parent.parent

# And add a line to load environment variables
load_dotenv(BASE_DIR / '.env')

# Replace sensitive things subsequently with os.getenv
SECRET_KEY = os.getenv('SECRET_KEY', 'Default Secret (not)')
ALLOWED_HOSTS = [os.getenv('ALLOWED_HOST')]
```

Note that AWS does not support SQLite and you will need to replace the database backend with something workable:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}
```
