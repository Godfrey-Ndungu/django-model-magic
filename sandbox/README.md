
# Django-Model-Magic Sandbox




## Environment  variables
To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`ALLOWED_HOSTS`


## Run Locally

Clone the project

```bash
  https://github.com/Godfrey-Ndungu/django-model-magic
```

1. manually

```bash
  cd django-model-magic
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  python3 manage.py migrate
  python manage.py runserver
```

2. Using makefile

```bash
  cd django-model-magic
  chmod +x makefile.sh
  ./makefile.sh
```

3. using docker
- make sure docker is installed

```bash
    docker build -t sandbox .
    docker run -p 8000:8000 sandbox
```


## Running Tests

To run tests, run the following command

```bash
  tox
```

