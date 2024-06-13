import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv()  # This loads the .env file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')

application = get_wsgi_application()
