cd ...-service
python -m venv venv
venv\Scripts\activate
pip install django==4.2 djangorestframework==3.14 django-channels==4.0 channels-redis==4.1 psycopg2-binary==2.9 confluent-kafka==2.1
django-admin startproject ..._service .
mkdir apps
cd apps
django-admin startapp ...