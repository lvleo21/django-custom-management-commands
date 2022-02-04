<h1 align="center">Writing custom management commands in Django</h1>

<p align="center">This project example will show how to add data from file json in your database through a django custom management commands.</p>


## Table of Contents

<!--ts-->
   * [Running this project](#running-this-project)
   * [Creating your custom command](#creating-your-custom-command)
<!--te-->

## Running this project

1. Clone project in your machine
2. Create and active the virtualenv from this command

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
5. Run the custom management command

```bash
  python manage.py load_data peoples.json
```

## Creating your custom command


1. In your project app, create directory called **management** and a child directory called **commands**

2. Create a python file with the name “my_command.py” (choose the name according to what your command is going to do) inside the commands directory

3. 


<h4 align="center"> 
	🚧  Readme in construction...  🚧
</h4>
