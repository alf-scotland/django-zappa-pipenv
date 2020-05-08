"""Storage configurations.

See https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html for details
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).absolute().parent.parent.parent

# Load local environment variables
load_dotenv(BASE_DIR / '.env')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')