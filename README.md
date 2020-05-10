# django-vue
# virtual environment

# Creates a virtual environment
  python3 -m venv env

# Activate the virtual environment
  source env/bin/activate

# Dependency Installation
  Use the package manager pip to install requirements.
  pip install -r requirements.txt

# DB Configurations
# settings.py
DATABASES = {
'default': {
'PORT': 3306,
'ENGINE': 'django.db.backends.mysql',
'OPTIONS':
{
'sql_mode': 'traditional',
},
'NAME': os.environ.get('DB_NAME', 'db_schema_name'),
'USER': os.environ.get('DB_USER', 'root'),
'PASSWORD': os.environ.get('DB_PASSWORD', ''),
'HOST': os.environ.get('DB_HOST', 'localhost'),
}
}

# Migrations
  python manage.py makemigrations

  python manage.py migrate

# To create admin user
  python manage.py createsuperuser

# To run server
  python manage.py runserver

# Endpoints

  To get all user
  {{url}}/api/v1/users/?page={page}&page_size={page_size}

  To get user by id
  {{url}}/api/v1/users/{id}

