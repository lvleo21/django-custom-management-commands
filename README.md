<h1 align="center">Writing custom management commands in Django</h1>

<p align="center">This project example will show how to add data from file json in your database through a django custom management commands.</p>

## Running Project

1. Clone project in your machine
2. create and run the virtualenv from this command

```bash
  python3 -m venv venv
  source venv/bin/activate
```

3. Install all required packages

```bash
  pip install -r requirements.txt
```

4. Create a sqlite database

```bash
  python manage.py migrate
```
5. Running a custom management command

```bash
  python manage.py load_data peoples.json
```
