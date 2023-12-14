# LAB - Class 27

## Project:


## Author:
Jacob Bassett

## Description:

This is a simple application to provide us practice leveraging Django Models within out projects.

## Setup:

The following commands will help you set up this application.

```bash
# clone the repository to your machine
git clone <repository url>
# create a virtual environment
python3.? -m venv .venv
# activate the virtual environment
source .venv/bin/activate
# install requirements
pip install -r requirements
# create database 
python3.? manage.py migrate
# create a user account
python3.? manage.py createsuperuser
# run server and open browser to 'http://127.0.0.1:8000'
python3.? manage.py runserver
# run tests with the following command
python3.? manage.py test
``` 